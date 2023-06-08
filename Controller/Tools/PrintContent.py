class PrintContent:
    def __init__(self, path) -> None:
        self.path = path

    def execute(self):
        f = open(self.path, 'r', encoding='utf8')
        return(f.read())