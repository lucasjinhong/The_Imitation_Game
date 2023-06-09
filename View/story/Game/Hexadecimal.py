from Controller.Controller import Controller

class Hexadecimal:
    def __init__(self, parameters):
        self.parameters = parameters
        self.text = ''
        self.button_enter = parameters['config']['button_enter']
        self.button_conti = parameters['config']['button_conti']
        self.next_choose = parameters['config']['next_choose']

    def before_scene(self):
        self.button_enter.setEnabled(False)

        path = 'Model/Story/Level1/Hexadecimal/BeforeScene.txt'
        self.text += Controller.tools(path)

        self.parameters['parameters'] = {
            'Level': 'hexadecimal',
            'Scene': '1'
        }

        return self.parameters, self.text

    def question_1(self):
        self.button_enter.setEnabled(True)
        self.button_conti.setEnabled(False)
        answer_hex, answer_dec = Controller.codec('hex_to_dec')

        self.text += '\n[第一關]\n'
        self.text += f'若一串十六進制數字為{answer_hex}，它代表的十進制數字是多少？\n'
    
        self.parameters['parameters'] = {
            'Level': 'hexadecimal',
            'Scene': '2'
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '恭喜你\n',
                'wrong': '答案錯誤\n',
                'answer': answer_dec,
                'hint': 'hint：每位數的十六進制數字都對應到一個0至15的十進制數字，並且每向左移一位，其值就增加16倍。\n',
                'solution': f'正確答案是：{answer_dec}\n'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }                  
        }

        return self.parameters, self.text

    def question_2(self):
        self.button_enter.setEnabled(True)
        self.button_conti.setEnabled(False)
        answer_dec, answer_hex = Controller.codec('dec_to_hex')

        self.text += '\n顯示板上又出現了一個更複雜的問題。\n\n'
        self.text += '[第二關]\n'
        self.text += f'若一串十進制數字為{answer_dec}，它代表的十六進制數字是多少？\n'

        self.parameters['parameters'] = {
            'Level': 'hexadecimal',
            'Scene': '3'
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '恭喜你\n',
                'wrong': '答案錯誤\n',
                'answer': answer_hex,
                'hint': 'hint：反覆除以16，看餘數，並反向排列所有的餘數\n',
                'solution': f'正確答案是：{answer_hex}\n'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }                  
        }

        return self.parameters, self.text

    def question_3(self):
        self.button_enter.setEnabled(True)
        self.button_conti.setEnabled(False)

        self.text += '\n你覺得應該結束了，十六進制應該就這樣了\n'
        self.text += '把十六進制轉成十進制，把十進制轉成十六進制，\n'
        self.text += '最重要的應該就是這兩個觀念，\n'
        self.text += '但這時，螢幕上出現了第三題：\n\n'
        self.text += '[第三關]\n'
        self.text += f'請問 1 + 1 = ？\n'
        self.text += '你心想，這個問題這麼簡單，毫不猶豫的輸入答案：\n'

        self.parameters['parameters'] = {
            'Level': 'hexadecimal',
            'Scene': 'after'
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '機器人：「你很勇嘛。」\n',
                'wrong': '機器人：「答案錯誤。」\n',
                'answer': '2',
                'hint': '',
                'solution': '機器人：「我看你是完全不懂喔。」\n機器人：「從第一關開始吧。」\n'
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

        if self.next_choose:
            self.parameters['parameters'] = {
                'Level': '1',
                'Scene': '2'
            }
        else:
            self.parameters['parameters'] = {
                'Level': '1',
                'Scene': '3'
            }

        return self.parameters, self.text