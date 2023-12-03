import json


class DataStorage:
    def __init__(self, path):
        self.__path = path
        self.status = 'disconnected'
        self.content = None
        self.new_file = None

    @property
    def path(self):
        return self.__path

    def _create_storage(self):
        with open(f'{self.path}', 'w') as new_file:
            json.dump([], new_file)
            return new_file

    def connect(self):
        try:
            self.new_file = open(f'{self.path}', 'r')
            new_content = json.load(self.new_file)
            self.content = new_content
        except FileNotFoundError:
            self._create_storage()
            self.connect()

    def disconnect(self):
        self.new_file.close()
        print('File close')


storage_one = DataStorage('new_file_one.json')
storage_one.connect()
storage_one.content
storage_one.disconnect()
