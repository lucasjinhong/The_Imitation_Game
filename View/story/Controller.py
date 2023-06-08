from View.Story.Level1 import Level1
from View.Story.Game.Binary import Binary
from View.Story.Game.Hexadecimal import Hexadecimal

class Controller:
    def __init__(self, parameters, text):
        self.parameters = parameters
        self.text = text
        self.label = parameters['config']['label']
        self.button_enter = parameters['config']['button_enter']
        self.button_conti = parameters['config']['button_conti']

    def scene_select(self):
        level = {
            '1': Level1(self.parameters, self.text),
            'binary': Binary(self.parameters, self.text),
            'hexadecimal': Hexadecimal(self.parameters, self.text)
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
            }
        }

        resp_level = self.parameters.get('parameters')['Level']
        resp_scene = self.parameters.get('parameters')['Scene']

        return scene[resp_level][resp_scene]()

    def question_select(self):
        question = self.parameters.get('parameters_game')['question']
        config = self.parameters.get('parameters_game')['config']

        chance =  config['chance']
        retry = config['retry']
        response = question['response']
        answer = question['answer']
        solution = question['solution']

        if response == answer:
            self.text += question['correct']
            self.button_enter.setEnabled(False)
            self.button_conti.setEnabled(True)
        else:
            self.text += question['wrong']

            if chance == 1:
                if retry == 1:
                    self.parameters['parameters']['Scene'] = '1'          #back to first stage

                self.text += solution
                self.button_enter.setEnabled(False)
                self.button_conti.setEnabled(True)
                
            elif chance <= 3:
                self.text += question['hint']

        self.label.setText(self.text)
        self.parameters['parameters_game']['config']['chance'] -= 1

        return self.parameters, self.text