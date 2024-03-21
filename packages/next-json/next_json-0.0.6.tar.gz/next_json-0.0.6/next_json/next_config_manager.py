import atexit
import threading

from next_json.next_json_obj import NextJson


class NextConfigManager:

    def __init__(self, file_path, instant_save=False):
        self.file_path = file_path
        self.instant_save = instant_save
        self.lock = threading.Lock()

        atexit.register(lambda: self.save())

        def on_set(key, value):
            if self.instant_save:
                self.save()

        try:
            with open(file_path, 'r') as file:
                self.config = NextJson(file.read())
        except FileNotFoundError:
            self.config = NextJson({})
        self.config.on('set', on_set)

    def save(self):
        with self.lock:
            with open(self.file_path, 'w') as file:
                file.write(str(self.config))
