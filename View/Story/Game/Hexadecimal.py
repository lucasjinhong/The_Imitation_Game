from Controller.Controller import Controller

class Hexadecimal:
    def __init__(self, parameters):
        self.parameters = parameters
        self.text = ''
        self.next_choose = parameters['config']['next_choose']

    def before_scene(self):
        path = 'Model/Story/Level1/Hexadecimal/BeforeScene.txt'
        self.text += Controller.tools(path)

        self.parameters['config']['button_enter'] = False
        self.parameters['config']['button_conti'] = True

        self.parameters['parameters'] = {
            'Level': 'hexadecimal',
            'Scene': '1',
            'last_question': '',
            'last_answer': ''
        }

        return self.parameters, self.text

    def question_1(self):
        answer_hex, answer_dec = Controller.codec('1', 'hex_to_dec')

        self.text += '[第一關]\n'
        self.text += f'若一串十六進制數字為{answer_hex.upper()}，它代表的十進制數字是多少？\n'
        self.text += '(請輸入3或4或5位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['parameters'] = {
            'Level': 'hexadecimal',
            'Scene': '2',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer_dec,
                'hint': '提示：每位數的十六進制數字都對應到一個0至15的十進制數字，並且每向左移一位，其值就增加16倍。',
                'solution': f'正確答案是：{answer_dec}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def question_2(self):
        answer_dec, answer_hex = Controller.codec('1', 'dec_to_hex')

        self.text += '顯示板上又出現了一個更複雜的問題。\n\n'
        self.text += '\n[第二關]\n'
        self.text += f'若一串十進制數字為{answer_dec}，它代表的十六進制數字是多少？\n'
        self.text += '(請輸入3或4位的數字或英文字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['parameters'] = {
            'Level': 'hexadecimal',
            'Scene': '3',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer_hex,
                'hint': '提示：反覆除以16，看餘數，並反向排列所有的餘數(英文字請用大寫)',
                'solution': f'正確答案是：{answer_hex}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def question_3(self):
        self.text += '你覺得應該結束了，十六進制應該就這樣了\n'
        self.text += '把十六進制轉成十進制，把十進制轉成十六進制，\n'
        self.text += '最重要的應該就是這兩個觀念，\n'
        self.text += '但這時，螢幕上出現了第三題：\n\n'

        self.text += '\n[第三關]\n'
        self.text += f'請問 1 + 1 = ？\n'
        self.text += '你心想，這個問題這麼簡單，毫不猶豫的輸入答案：\n'
        self.text += '(請輸入1或2位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['parameters'] = {
            'Level': 'hexadecimal',
            'Scene': 'after',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': '2',
                'hint': '',
                'solution': '機器人：「我看你是完全不懂喔。」\n機器人：「從第一關開始吧。」'
            },
            'config': {
                'chance': 3,
                'retry': 1
            }
        }

        return self.parameters, self.text

    def after_scene(self):
        path = 'Model/Story/Level1/Hexadecimal/AfterScene.txt'
        self.text += Controller.tools(path)

        self.parameters['config']['button_enter'] = False
        self.parameters['config']['button_conti'] = True

        if self.next_choose:
            self.parameters['parameters'] = {
                'Level': '1',
                'Scene': '2',
                'last_question': '',
                'last_answer': ''
            }
        else:
            self.parameters['parameters'] = {
                'Level': '1',
                'Scene': '3',
                'last_question': '',
                'last_answer': ''
            }

        return self.parameters, self.text

    def scene_handler(self):
        resp_scene = self.parameters.get('parameters')['Scene']

        scene = {
            'before': self.before_scene,
            '1': self.question_1,
            '2': self.question_2,
            '3': self.question_3,
            'after': self.after_scene
        }

        return scene[resp_scene]()