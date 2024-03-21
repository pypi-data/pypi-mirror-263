import atexit
import threading

from next_dict.next_dict_obj import NextDict


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
                self.config = NextDict(file.read(), on_set)
        except FileNotFoundError:
            self.config = NextDict({}, on_set)

    def save(self):
        with self.lock:
            with open(self.file_path, 'w') as file:
                file.write(str(self.config))
