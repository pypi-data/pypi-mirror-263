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
        self.emit('get', key, default)
        if key in self.__dict_data:
            return self.__dict_data[key]
        return default

    def set(self, key, value):
        key = str(key)
        if not self.is_json_serializable(value) and not isinstance(value, NextJson):
            value = str(value)
        self.emit('set', key, value)
        self.__dict_data[key] = value

    def __delitem__(self, key):
        if key not in self.__dict_data:
            return
        self.emit('del', key)
        del self.__dict_data[key]

    def __contains__(self, key):
        return key in self.__dict_data

    def __str__(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def __bool__(self):
        return bool(self.__dict_data)

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

    def to_dict(self):
        return self.__dict_manager.to_dict()

    def on(self, name, listener):
        self.__dict_manager.on(name, listener)

    def once(self, event_name, listener):
        self.__dict_manager.once(event_name, listener)

    def off(self, event_name, listener):
        self.__dict_manager.off(event_name, listener)

    def replace_data(self, data):
        self.__dict_manager = JsonDictManager(data)

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
