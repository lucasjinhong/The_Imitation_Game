import os

class PrintContent:
    def __init__(self, path) -> None:
        self.path = path

    def execute(self):
        path_temp = self.path.split('/')
        self.path = path_temp[0]
        path_temp.pop(0)

        for name in path_temp:
            self.path = os.path.join(self.path, name)

        f = open(self.path, 'r', encoding='utf8')
        return(f.read())