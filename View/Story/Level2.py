from Controller.Controller import Controller

class Level2:
    def __init__(self, parameters):
        self.parameters = parameters
        self.text = ''
        self.last_question = parameters['parameters']['last_question']
        self.last_answer = parameters['parameters']['last_answer']

    def scene_1(self):
        path = 'Model/Story/Level2/Scene1.txt'
        self.text += Controller.tools(path)

        self.parameters['config']['button_enter'] = False
        self.parameters['config']['button_conti'] = True

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': '2',
            'last_question': '',
            'last_answer': ''
        }

        return self.parameters, self.text

    def scene_2(self):
        answer, question = Controller.codec('2', 'not_gate')

        self.text += '在Binaropolis的中心，居民們正為如何對抗那個黑客而煩惱著。'
        self.text += '而就在此時，一道訊號忽然出現在一條被命名為 "Negation Alley" 的巷子中。'
        self.text += f'這個訊號源自那位神秘的黑客，他留下了一串二進制碼："{question[0]}"。\n\n'

        path = 'Model/Story/Level2/Scene2.txt'
        self.text += Controller.tools(path)

        self.text += f'\n這串二進制碼 "{question[0]}" 在Not英雄的能力作用下，會變成怎樣的結果？\n'
        self.text += f'(請輸入8位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': '3',
            'last_question': question[0],
            'last_answer': answer
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：Not的能力代表著否定，1的否定為0；0的否定為1',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_3(self):
        answer, question = Controller.codec('2', 'and_gate', [self.last_answer])

        self.text += 'Not伸出手指輕觸數據流，然後，一股強大的能量釋放出來。'
        self.text += f'在他的能力作用下，原本的 {self.last_question} 被反轉為了 {self.last_answer}。\n\n'

        path = 'Model/Story/Level2/Scene3-1.txt'
        self.text += Controller.tools(path)

        self.text += f'\n這兩組訊號分別是 "{question[1]}" 和經Not轉換過的 "{question[0]}" 。'
        self.text += '二者被黑客巧妙地連接在一起，每一個數字都對應著另一組數字的相應位置。'
        self.text += '這種關聯似乎並不隨機，而是有特定的規律。\n\n'

        path = 'Model/Story/Level2/Scene3-2.txt'
        self.text += Controller.tools(path)

        self.text += f'\n這兩串二進制碼 "{question[1]}" , "{question[0]}" 在And的能力作用下，會變成怎樣的結果？\n'
        self.text += f'(請輸入8位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': '4',
            'last_question': '',
            'last_answer': answer
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：And的能力代表著交集，當兩個數字都為1是，結果才為1，否則結果為0',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_4(self):
        answer, question = Controller.codec('2', 'or_gate', [self.last_answer])

        self.text += '眾人屏息以待，And 終於開口：「我完成了運算。」'
        self.text += f'他指著新的二進制碼 {question[0]} 說道：「這是我根據這兩串數字運算的結果。'
        self.text += '我相信，這將帶給我們新的線索，也將使我們更接近真相。」\n\n'

        path = 'Model/Story/Level2/Scene4-1.txt'
        self.text += Controller.tools(path)

        self.text += f'\n在他們沿著 Union Avenue 深入的時候，一個新的訊號忽然閃爍著微弱的光芒出現在他們的眼前，那是一串二進制碼： "{question[0]}" 。'
        self.text += '此時，他們看到黑客留下的另一個訊息：「在聯合中取得答案。」\n\n'
        self.text += '這似乎是個新的提示，也可能是另一個陷阱，'
        self.text += '無論如何，他們必須前進，他們必須去解開這個新的謎團。'
        self.text += '二者被黑客巧妙地連接在一起，每一個數字都對應著另一組數字的相應位置。'
        self.text += '這種關聯似乎並不隨機，而是有特定的規律。\n\n'

        path = 'Model/Story/Level2/Scene4-2.txt'
        self.text += Controller.tools(path)

        self.text += f'\n如果將 And 處理過的二進制碼 "{question[0]}" 和新的訊號 "{question[1]}" 進行Or的能力，會變成怎樣的結果？\n'
        self.text += f'(請輸入8位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': '5',
            'last_question': '',
            'last_answer': answer
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：Or的能力代表著聯集，只要其中一個數字是1，結果就是1',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_5(self):
        answer, question = Controller.codec('2', 'xor_gate', [self.last_answer])

        self.text += f'瞬間，邏輯或運算的結果出現在他們面前，新的二進制碼清晰可見，那就是 {question[0]} 。'
        self.text += 'Or深深地吸了口氣，轉向他的隊友們，他的聲音充滿了自信與堅定，「答案，已經出現。」\n\n'

        path = 'Model/Story/Level2/Scene5-1.txt'
        self.text += Controller.tools(path)

        self.text += f'\n突然，他們的道路上出現了一個新的訊號，一串二進制碼："{question[1]}"。'
        self.text += '這串碼與Or處理過的結果在空氣中相遇，形成了新的混淆碼，引起了他們的注意。\n\n'
        self.text += '同時，一段神秘的信息出現在他們的腦海中：「在分歧中尋找一致。」他們瞬間認出，這是黑客的新線索。\n\n'

        path = 'Model/Story/Level2/Scene5-2.txt'
        self.text += Controller.tools(path)

        self.text += f'\n請試著將 Or 處理過的二進制碼 "{question[0]}" 和新訊號 "{question[1]}" 進行Xor的能力運算，會變成怎樣的結果？\n'
        self.text += f'(請輸入8位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': '6',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：Xor的能力代表著互斥或，相同為0，相異為1',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_6(self):
        answer, question = Controller.codec('2', 'hex_to_bin')

        path = 'Model/Story/Level2/Scene6.txt'
        self.text += Controller.tools(path)

        self.text += f'這個混淆碼是一串16進制碼： "{question}" ，'
        self.text += '旁邊還寫著一個訊息：「只有那些能理解我們的語言，才能找到我們。」\n\n'
        self.text += '看來，他們需要先將這串混淆碼做一些轉換，才能進行運算。\n'
        self.text += '請輸入這串16進制碼轉成2進制碼後的結果：\n'
        self.text += '(以8位數字為一組，每一組之間空一個半形空格，\n'
        self.text += ' Ex：00000000 11111111 00000000 11111111)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': '7',
            'last_question': question,
            'last_answer': answer
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：一位16進制碼為4位2進制碼(A: 10, B:11, C: 12, D: 13, E: 14, F: 15)',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_7(self):
        question = self.last_answer.split(' ')
        answer = Controller.codec('2', 'all_in_one', question)

        self.text += '四位英雄一起上前，他們集中了全力，將這串16進制碼轉換為2進制碼，他們知道，16進制的每一個數字或字母代表4個2進制碼。'
        self.text += f'所以，這串16進制碼 {self.last_question} 轉成2進制碼後的結果為：{self.last_answer}。\n\n'

        path = 'Model/Story/Level2/Scene7.txt'
        self.text += Controller.tools(path)

        self.text += '現在，請根據之前的訊息，填入下面這四個空格：\n\n'
        self.text += f'1. 最一開始出現的是 {question[0]} ，經過Not能力運算後，得到 `A`\n'
        self.text += f'2. 把 `A` 和 {question[1]} 進行And能力運算後，得到 `B`\n'
        self.text += f'3. 把 `B` 和 {question[2]} 進行Or能力運算後，得到 `C`\n'
        self.text += f'4. 把 `C` 和 {question[3]} 進行Xor能力運算後，得到 `D`\n\n'
        self.text += '請照順序輸入A, B, C, D：\n'
        self.text += '(以8位數字為一組，每一組之間空一個半形空格，\n'
        self.text += ' Ex：00000000 11111111 00000000 11111111)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': '8',
            'last_question': self.last_answer,
            'last_answer': answer
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：\nNot：0變1；1變0\nAnd：都是1才是1，只要其中一個是0就是0\nOr：都是0才是0，只要其中一個是1就是1\nXor：相同為0，相異為1',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_8(self):
        path = 'Model/Story/Level2/Scene8-1.txt'
        self.text += Controller.tools(path)

        self.text += '\n四位英雄對視一眼，他們知道，這一次的挑戰將比之前的還要艱鉅。'
        self.text += '這不僅僅是一場對他們理解力和運算能力的考驗，更是對他們堅韌意志的挑戰。\n\n'
        self.text += f'他們再次集中全力，將先前從16進制轉換為的2進制碼 {self.last_question} 以及解答 {self.last_answer} ──── A, B, C, D '
        self.text += '進行Not, And, Or, Xor的運算，然而，嘗試了幾次之後，很快就發現事情沒有這麼簡單。\n\n'

        path = 'Model/Story/Level2/Scene8-2.txt'
        self.text += Controller.tools(path)

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': '9',
            'last_question': self.last_question,
            'last_answer': self.last_answer
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': '4231',
                'hint': '',
                'solution': '正確答案是：4231'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_9(self):
        question = [self.last_question.split(' '), self.last_answer.split(' ')]
        question[1][3] = '________'
        self.last_answer = ' '.join(question[1])
        answer = Controller.codec('2', 'last_codec', question)

        path = 'Model/Story/Level2/Scene9.txt'
        self.text += Controller.tools(path)

        self.text += '\n請輸入這兩段數字，經過Xor And Or Not運算後的結果\n'
        self.text += f' "{self.last_question}" 和\n'
        self.text += f' "{self.last_answer}" ──── A, B, C, D\n'
        self.text += '(由於Not英雄提出 D 組數字可能存在錯誤，該組數字已經被屏蔽。)\n\n'

        self.text += '(以8位數字為一組，每一組之間空一個半形空格，\n'
        self.text += ' Ex：00000000 11111111 00000000 11111111)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '2',
            'Scene': 'after',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：\nNot：0變1；1變0\nAnd：都是1才是1，只要其中一個是0就是0\nOr：都是0才是0，只要其中一個是1就是1\nXor：相同為0，相異為1',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def after_scene(self):
        path = 'Model/Story/Level2/AfterScene.txt'
        self.text += Controller.tools(path)

        self.parameters['config']['button_enter'] = False
        self.parameters['config']['button_conti'] = False

        return self.parameters, self.text

    def scene_handler(self):
        resp_scene = self.parameters.get('parameters')['Scene']

        scene = {
            '1': self.scene_1,
            '2': self.scene_2,
            '3': self.scene_3,
            '4': self.scene_4,
            '5': self.scene_5,
            '6': self.scene_6,
            '7': self.scene_7,
            '8': self.scene_8,
            '9': self.scene_9,
            'after': self.after_scene
        }

        return scene[resp_scene]()