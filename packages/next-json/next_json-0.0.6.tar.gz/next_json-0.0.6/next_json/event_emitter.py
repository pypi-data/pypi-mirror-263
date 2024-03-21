class EventEmitter:
    __listeners = {}

    def __init__(self):
        self.__listeners = {}

    def on(self, event_name, listener):
        if event_name not in self.__listeners:
            self.__listeners[event_name] = []

        self.__listeners[event_name].append(listener)
        return

    def once(self, event_name, listener):
        def once_listener(*args):
            listener(*args)
            self.off(event_name, once_listener)

        self.on(event_name, once_listener)

    def off(self, event_name, listener):
        if event_name in self.__listeners:
            self.__listeners[event_name].remove(listener)

    def emit(self, event_name, *args):
        listeners = self.__listeners.get(event_name)

        if listeners is not None:
            for listener in listeners:
                listener(*args)
