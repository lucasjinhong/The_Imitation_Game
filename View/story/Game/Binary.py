from Controller.Controller import Controller

class Binary:
    def __init__(self, parameters, text):
        self.parameters = parameters
        self.text = text
        self.label = parameters['config']['label']
        self.button_enter = parameters['config']['button_enter']
        self.button_conti = parameters['config']['button_conti']
        self.next_choose = parameters['config']['next_choose']

    def before_scene(self):
        self.button_enter.setEnabled(False)

        path = 'Model/Story/Level1/Binary/BeforeScene.txt'
        self.text += Controller.tools(path)
        self.label.setText(self.text)

        self.parameters['parameters'] = {
            'Level': 'binary',
            'Scene': '1'
        }

        return self.parameters, self.text

    def question_1(self):
        self.button_enter.setEnabled(True)
        self.button_conti.setEnabled(False)
        answer_bin, answer_dec = Controller.codec('bin_to_dec')

        self.text += '\n[第一關]\n'
        self.text += f'若一串二進制數字為{answer_bin}，它代表的十進制數字是多少？\n'
        self.label.setText(self.text)
    
        self.parameters['parameters'] = {
            'Level': 'binary',
            'Scene': '2'
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '恭喜你\n',
                'wrong': '答案錯誤\n',
                'answer': answer_dec,
                'hint': '\nhint：每左移一個數字，就是前一個數字的兩倍\n',
                'solution': f'\n正確答案是：{answer_dec}\n'
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
        answer_dec, answer_bin = Controller.codec('dec_to_bin')

        self.text += '\n這時，螢幕上又繼續顯示了下一題。\n\n'
        self.text += '[第二關]\n'
        self.text += f'若一串十進制數字為{answer_dec}，它代表的二進制數字是多少？\n'
        self.label.setText(self.text)

        self.parameters['parameters'] = {
            'Level': 'binary',
            'Scene': '3'
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '恭喜你\n',
                'wrong': '答案錯誤\n',
                'answer': answer_bin,
                'hint': '\nhint：反覆除以2，看餘數，並反向排列所有的餘數\n',
                'solution': f'\n正確答案是：{answer_bin}\n'
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

        self.text += '\n你覺得應該結束了，二進制應該就這樣了，\n'
        self.text += '把二進制轉成十進制，把十進制轉成二進制，\n'
        self.text += '最重要的應該就是這兩個觀念，\n'
        self.text += '但這時，螢幕上出現了第三題：\n\n'
        self.text += '[第三關]\n'
        self.text += f'請問 1 + 1 = ？\n'
        self.text += '你心想，這個問題這麼簡單，毫不猶豫的輸入答案：\n'
        self.label.setText(self.text)

        self.parameters['parameters'] = {
            'Level': 'binary',
            'Scene': 'after'
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '機器人：「你很勇嘛。」\n',
                'wrong': '機器人：「答案錯誤。」\n',
                'answer': '10',
                'hint': '',
                'solution': '\n機器人：「我看你是完全不懂喔。」\n機器人：「從第一關開始吧。」\n'
            },
            'config': {
                'chance': 3,
                'retry': 1
            }                
        }

        return self.parameters, self.text

    def after_scene(self):
        path = 'Model/Story/Level1/Binary/AfterScene.txt'
        self.text += Controller.tools(path)
        self.label.setText(self.text)

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