from Model.Text.Random import Random
from Controller.Level.Level1 import Level1
from Controller.Level.Level2 import Level2
from Controller.Level.Level3 import Level3

class Controller:
    def __init__(self, level):
        self.level = level

    def execute(self):
        method = {
            '1': Level1,
            '2': Level2,
            '3': Level3
        }

        rand = Random()
        word = rand.random_word()

        try:
            method[self.level](word).execute()
        except Exception as e:
            print(f'{e} is not acceptable')
