from View.Story.Level1 import Level1
from View.Story.Level2 import Level2
from View.Story.Game.Binary import Binary
from View.Story.Game.Hexadecimal import Hexadecimal

class Controller:
    def __init__(self, parameters):
        self.parameters = parameters
        self.text = ''

    def scene_select(self):
        level = {
            '1': Level1(self.parameters),
            'binary': Binary(self.parameters),
            'hexadecimal': Hexadecimal(self.parameters),
            '2': Level2(self.parameters)
        }

        scene = {
            '1': {
                '1': level['1'].scene_1,
                '2': level['1'].scene_2,
                '3': level['1'].scene_3,
                'after': level['1'].after_scene
            },
            'binary': {
                'before': level['binary'].before_scene,
                '1': level['binary'].question_1,
                '2': level['binary'].question_2,
                '3': level['binary'].question_3,
                'after': level['binary'].after_scene,
            },
            'hexadecimal': {
                'before': level['hexadecimal'].before_scene,
                '1': level['hexadecimal'].question_1,
                '2': level['hexadecimal'].question_2,
                '3': level['hexadecimal'].question_3,
                'after': level['hexadecimal'].after_scene,
            },
            '2': {
                '1': level['2'].scene_1,
                '2': level['2'].scene_2,
                '3': level['2'].scene_3,
                '4': level['2'].scene_4,
                '5': level['2'].scene_5,
                '6': level['2'].scene_6,
                '7': level['2'].scene_7
            }
        }

        resp_level = self.parameters.get('parameters')['Level']
        resp_scene = self.parameters.get('parameters')['Scene']

        return scene[resp_level][resp_scene]()

    def question_select(self):
        question = self.parameters.get('parameters_game')['question']
        games_config = self.parameters.get('parameters_game')['config']

        chance =  games_config['chance']
        retry = games_config['retry']
        response = question['response']
        answer = str(question['answer'])
        solution = question['solution']

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        if response == answer:
            self.text += question['correct']
            self.parameters['config']['button_enter'] = False
            self.parameters['config']['button_conti'] = True
        else:
            self.text += question['wrong']

            if chance == 1:
                if retry == 1:
                    self.parameters['parameters']['Scene'] = '1'          #back to first stage

                self.text += '\n' + solution
                self.parameters['config']['button_enter'] = False
                self.parameters['config']['button_conti'] = True

            elif chance <= 3:
                self.text += '\n' + question['hint']

        self.parameters['parameters_game']['config']['chance'] -= 1

        return self.parameters, self.text
