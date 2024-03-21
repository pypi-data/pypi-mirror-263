import json

from next_json.event_emitter import EventEmitter


class JsonDictManager(EventEmitter):
    __dict_data = {}

    def __init__(self, value=None):
        super().__init__()
        if not value:
            value = {}
        if type(value) is dict:
            self.__dict_data = value
        elif type(value) is str:
            self.__dict_data = json.loads(value)
        elif type(value) is NextJson:
            self.__dict_data = value.to_dict()
        else:
            raise Exception("JsonDictManager load json error")

    @staticmethod
    def is_json_serializable(data):
        try:
            json.dumps(data)
            return True
        except TypeError:
            return False

    def get(self, key, default=None):
        key = str(key)
        result = default
        if key in self.__dict_data:
            result = self.__dict_data[key]
        self.emit('get', key, default, result)
        return result

    def set(self, key, value):
        key = str(key)
        self.__dict_data[key] = value
        self.emit('set', key, value)

    def delete(self, key):
        if key not in self.__dict_data:
            return False
        self.emit('del', key)
        del self.__dict_data[key]
        return True

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return key in self.__dict_data

    def __str__(self):
        return self.to_json()

    def __bool__(self):
        return bool(self.__dict_data)

    def get_data(self):
        return self.__dict_data

    def to_json(self):
        converted = {}
        for k, v in self.to_dict().items():
            if not self.is_json_serializable(v):
                v = str(v)
            converted[k] = v
        return json.dumps(converted, ensure_ascii=False)

    def to_dict(self):
        converted = {}
        for k, v in self.__dict_data.items():
            if isinstance(v, NextJson):
                v = v.to_dict()
            converted[k] = v
        return converted


class NextJson:
    __dict_manager = {}
    __index = 0

    def __init__(self, value=None, **values):
        self.__dict_manager = JsonDictManager(value or values)

    def get(self, key, default=None):
        result = self.__getattr__(key)
        return result if result else default

    def set(self, key, value):
        return self.__setattr__(key, value)

    def set_default(self, key, value=None):
        if key in self:
            return False
        self[key] = value
        return True

    def to_dict(self):
        return self.__dict_manager.to_dict()

    def to_json(self):
        return self.__dict_manager.to_json()

    def on(self, name, listener):
        self.__dict_manager.on(name, listener)

    def once(self, event_name, listener):
        self.__dict_manager.once(event_name, listener)

    def off(self, event_name, listener):
        self.__dict_manager.off(event_name, listener)

    def replace_data(self, data):
        self.__dict_manager = JsonDictManager(data)

    def keys(self):
        return self.__dict_manager.get_data().keys()

    def values(self):
        return self.__dict_manager.get_data().values()

    def items(self):
        return self.__dict_manager.get_data().items()

    def update(self, value=None, **values):
        update_params = NextJson(value or values)
        return self.__dict_manager.get_data().update(update_params.to_dict())

    def popitem(self):
        return self.__dict_manager.get_data().popitem()

    def copy(self):
        return NextJson(self)

    def pop(self, key, default=None):
        result = self[key]
        if result is None:
            return default
        del self[key]
        return result

    def __contains__(self, key):
        return key in self.__dict_manager

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __str__(self):
        return str(self.__dict_manager)

    def __bool__(self):
        return bool(self.__dict_manager)

    def __iter__(self):
        self.__index = 0
        return self

    def __len__(self):
        return len(self.to_dict())

    def __delitem__(self, key):
        del self.__dict_manager[key]

    def __delattr__(self, key):
        del self.__dict_manager[key]

    def __next__(self):
        if self.__index < len(self):
            key = list(self.to_dict().keys())[self.__index]
            self.__index += 1
            return key
        else:
            raise StopIteration

    def __getattr__(self, key):
        key = str(key)
        if key.startswith('_NextJson__'):
            return self.__dict__[key]
        value = self.__dict_manager.get(key, {})
        if type(value) is dict:
            result = NextJson(value)
            result.on('set', lambda x, y: self.set(key, result))
            # self.__dict_manager.set(key, result)
            return result
        return value

    def __setattr__(self, key, value):
        key = str(key)
        if key.startswith('_NextJson__'):
            self.__dict__[key] = value
            return
        self.__dict_manager.set(key, value)
