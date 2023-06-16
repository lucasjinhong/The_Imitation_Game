from View.Story.Level1 import Level1
from View.Story.Level2 import Level2
from View.Story.Level3 import Level3
from View.Story.Game.Binary import Binary
from View.Story.Game.Hexadecimal import Hexadecimal

class Controller:
    def __init__(self, parameters):
        self.parameters = parameters
        self.text = ''

    def scene_select(self):
        level = {
            '1': Level1(self.parameters).scene_handler,
            '2': Level2(self.parameters).scene_handler,
            '3': Level3(self.parameters).scene_handler,
            'binary': Binary(self.parameters).scene_handler,
            'hexadecimal': Hexadecimal(self.parameters).scene_handler
        }

        resp_level = self.parameters.get('parameters')['Level']

        return level[resp_level]()

    def question_select(self):
        question = self.parameters.get('parameters_game')['question']
        games_config = self.parameters.get('parameters_game')['config']

        chance =  games_config['chance']
        retry = games_config['retry']
        response = question['response']
        answer = str(question['answer']).lower()
        solution = question['solution']

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False
        self.parameters['config']['button_help'] = True

        if response == answer:
            self.text += question['correct']
            self.parameters['config']['button_enter'] = False
            self.parameters['config']['button_conti'] = True
            self.parameters['config']['button_help'] = False
        else:
            self.text += question['wrong']

            if chance == 1:
                if retry == 1:
                    self.parameters['parameters']['Scene'] = '1'          #back to first stage

                self.text += '\n' + solution
                self.parameters['config']['button_enter'] = False
                self.parameters['config']['button_conti'] = True

            # elif chance <= 3:
            #     self.parameters['config']['button_help'] = True

        self.parameters['parameters_game']['config']['chance'] -= 1

        return self.parameters, self.text
