from Controller.Controller import Controller

class Level3:
    def __init__(self, parameters):
        self.parameters = parameters
        self.text = ''
        self.last_question = parameters['parameters']['last_question']
        self.last_answer = parameters['parameters']['last_answer']

    def scene_1(self):
        path = 'Model/Story/Level3/Scene1.txt'
        self.text += Controller.tools(path)

        self.parameters['config']['button_enter'] = False
        self.parameters['config']['button_conti'] = True

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
            'Scene': '2',
            'last_question': '',
            'last_answer': ''
        }

        return self.parameters, self.text

    def scene_2(self):
        answer, question = Controller.codec('3', 'majority_vote')

        path = 'Model/Story/Level3/Scene2.txt'
        self.text += Controller.tools(path)

        self.text += '如果出現的訊號是：\n'
        self.text += f'嘗試 1 ： {question[0]}\n'
        self.text += f'嘗試 2 ： {question[1]}\n'
        self.text += f'嘗試 3 ： {question[2]}\n'
        self.text += f'嘗試 4 ： {question[3]}\n'
        self.text += f'嘗試 5 ： {question[4]}\n\n'

        self.text += f'請輸入接收端收到的訊號(用多數決)：\n'
        self.text += '(請輸入8位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
            'Scene': '3',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：共有8位數字，每一位數字都傳了5次。在這5次裡面，只要出現3, 4, 5次以上的1，接收端就把這位數字決定為1，也就是這位數字接收到的5次訊號裡面，哪一個出現次數比較多，就把它定義成這個數字，這就是「多數決」。',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_3(self):
        answer, question = Controller.codec('3', 'nand_gate')

        path = 'Model/Story/Level3/Scene3.txt'
        self.text += Controller.tools(path)

        self.text += '\n經過無數個日夜的觀察和分析，在一個普通的日子裡，就在早上7點。'
        self.text += '那時，他們正在密切監視NAND，突然，他們發現他的眼神中閃爍著一種不尋常的光芒。'
        self.text += f'他的身體開始震動，同時他們的程式也感測到了一組異常的2進制碼，也就是 "{question[0]}" 與 "{question[1]}" 。'
        self.text += '這兩組碼在他們的程式中形成了一個模式，與NAND的正常行為模式完全不同。\n\n'

        self.text += '這一發現讓他們如臨大敵，他們知道，這就是他們一直在尋找的線索。'
        self.text += '他們需要將這兩組二進制碼進行NAND運算，並試圖透過結果解析出黑客的傀儡碼。\n\n'

        self.text += f'請輸入 "{question[0]}" 和 "{question[1]}" 經過NAND運算後的結果：\n'
        self.text += '(請輸入8位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
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
                'hint': '提示：之前的And是都是1才是1，而只要有0就是0，現在在後面多一個Not，就是NAND，如果有困難的話，可以先把兩組數字都先做And運算，最後再把結果經過Not。',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_4(self):
        answer, question = Controller.codec('3', 'nor_gate')

        self.text += f'進行NAND運算後，他們得到的結果是 {self.last_answer} 。這一結果讓他們驚訝，同時也讓他們充滿了希望。'
        self.text += '他們知道，這個結果可能就是解開NAND傀儡碼的關鍵。\n\n'

        path = 'Model/Story/Level3/Scene4-1.txt'
        self.text += Controller.tools(path)

        self.text += '\n\n隨著日光越來越強烈，時間悄悄的走到了中午12點。'
        self.text += '這時，Or的行為開始出現異常，就像他們預期的一樣。他的動作變得機械，語言變得冷漠，這些都是黑客控制的明顯痕跡。'
        self.text += f'然而，他們的程式在這時也感測到了兩組新的二進制碼： "{question[0]}" 與 "{question[1]}" 。\n\n'

        path = 'Model/Story/Level3/Scene4-2.txt'
        self.text += Controller.tools(path)

        self.text += '\n這一發現讓他們如臨大敵，他們知道，這就是他們一直在尋找的線索。'
        self.text += '他們需要將這兩組二進制碼進行NOR運算，並試圖透過結果解析出黑客的傀儡碼。\n\n'

        self.text += f'請輸入 "{question[0]}" 和 "{question[1]}" 經過NOR運算後的結果：\n'
        self.text += '(請輸入8位數字)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
            'Scene': '5',
            'last_question': question,
            'last_answer': answer
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：可以將兩組數字經過Or運算後，再經過Not',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_5(self):
        answer, question = Controller.codec('3', 'xor_xnor_gate')

        self.text += f'當 {self.last_question[0]} 與 {self.last_question[1]} 經過NOR運算後，得到 {self.last_answer} ，Not和Buffer立即將解碼後的訊息重新傳輸給Or。'
        self.text += '然而，這一次的結果並不如他們所預期。雖然Or的表情稍微有些改變，但他的行為還是同樣機械，顯然他仍然處於黑客的控制之下。\n\n'

        path = 'Model/Story/Level3/Scene5-1.txt'
        self.text += Controller.tools(path)

        self.text += '\n\n這次他們的程式偵測到了五組異常的二進制碼，'
        self.text += f'分別是 "{question[0]}" , "{question[1]}" , "{question[2]}" , "{question[3]}" 以及 "{question[4]}" 。'
        self.text += '這些碼不僅數量比以往多，而且在他們的系統中也形成了一種新的、更複雜的模式。\n\n'

        path = 'Model/Story/Level3/Scene5-2.txt'
        self.text += Controller.tools(path)

        self.text += f'\n\n1. "{question[0]}" 和 "{question[1]}" 經過Xor運算的結果為 `A`\n'
        self.text += f'2. `A` 和 "{question[2]}" 經過XNOR運算的結果為 `B`\n'
        self.text += f'3. `B` 和 "{question[3]}" 經過Xor運算後的結果為 `C`\n'
        self.text += f'4. `C` 和 "{question[4]}" 經過XNOR運算後的結果為 `D`\n\n'

        self.text += '請依序輸入A, B, C, D：\n'
        self.text += '(以8位數字為一組，每一組之間空一個半形空格，\n'
        self.text += 'Ex：00000000 11111111 00000000 11111111)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
            'Scene': '6',
            'last_question': '',
            'last_answer': answer
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：XNOR可以將兩組數字經過Xor運算後，再經過Not，也就是相同為1，相異為0',
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_6(self):
        answer, question = Controller.codec('3', 'buffer_gate')

        path = 'Model/Story/Level3/Scene6-1.txt'
        self.text += Controller.tools(path)

        self.text += f'\n\n但這次沒有出現二進制碼，而是出現一群看不懂的英文字 "{question[0]}" ，但Not和Buffer知道，每一個字母代表著他們需要進行的運算。\n'
        self.text += '("N"代表NAND運算)\n'
        self.text += '("O"代表NOR運算)\n'
        self.text += '("X"代表XNOR運算)\n'
        self.text += '("T"代表Not運算)\n\n'

        path = 'Model/Story/Level3/Scene6-2.txt'
        self.text += Controller.tools(path)

        self.text += f'\n\n現在，你需要讓 "{question[0]}" 可以順利傳完，且在傳遞的過程中，能量不能≤0，你需要用最少的Buffer來達到這個效果，你一開始的能量有6。\n'
        self.text += '\n(T耗1能量，O耗2能量，N耗3能量，X耗4能量，\n'
        self.text += ' 而使用B可以補充6個能量，不能讓能量≤0)\n\n'

        self.text += f'請輸入 "{question[0]}" 加上Buffer後的英文代碼：\n'
        self.text += f'(請輸入共{len(answer)}個英文代碼)'

        hint = '提示：\n'
        hint += 'T：1　O：2　N：3　X：4\n'
        hint += '起始能量是6，每一次使用T, O, N, X都會耗掉相應的能量，而不能讓能量≤0，如果扣掉下一個傳遞能量會≤0，就加上一個B(Buffer)在前面\n'
        hint += '(EX：如果前三個字母是NOX，需要在NO和X中間加上B，變成NOBX，因為N會耗3個能量，O會耗2個能量，\n'
        hint += '這樣6 - 3 - 2 = 1，對下一個X來說能量不夠，所以需要在NO和X中間加上一個B)\n'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
            'Scene': '7',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': hint,
                'solution': f'正確答案是：{answer}'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_7(self):
        answer = 'gedhfe'

        path = 'Model/Story/Level3/Scene7.txt'
        self.text += Controller.tools(path)

        self.text += '\n\n請將這個 "Xor, NAND, Not, Or, Not, XNOR, NOR, Not, Buffer, And" 邏輯順序，在不影響運算結果的情況下，用「最少的」邏輯閘順序來呈現：\n\n'

        path = 'Model/Story/Level3/Scene7-ax.txt'
        self.text += Controller.tools(path)

        hint = '提示：\n'
        hint += 'Buffer在不考慮能量的情況下，可以忽略\n'
        hint += 'Not, Not可以合併成Buffer\n'
        hint += 'And, Not可以合併成NAND\n'
        hint += 'Or, Not可以合併成NOR\n'
        hint += 'Xor, Not可以合併成XNOR\n'
        hint += 'NAND, Not可以合併成And\n'
        hint += 'NOR, Not可以合併成Or\n'
        hint += 'XNOR, Not可以合併成Xor\n'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
            'Scene': '7-1',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': hint,
                'solution': f'正確答案是：{answer}\n(Xor, And, NOR, XNOR, Or, And)'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_7_1(self):
        answer = '26'

        path = 'Model/Story/Level3/Scene7-ex.txt'
        self.text += Controller.tools(path)

        self.text += '\n(請輸入這6個邏輯閘的能量損耗加總)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
            'Scene': '8',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': '提示：出現什麼邏輯閘，就把上面對應的數字加總',
                'solution': f'正確答案是：{answer}\n(5 + 4 + 2 + 7 + 4 + 4)'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_8(self):
        answer = 'gcadhdae'

        self.text += '請將這個"Xor, NAND, Not, Or, Not, XNOR, NOR, Not, Buffer, And"邏輯順序，在不影響運算結果的情況下，用「最快的」邏輯閘順序來呈現：\n'
        self.text += '(也就是能量損耗加總「最低」的邏輯)\n\n'

        path = 'Model/Story/Level3/Scene7-bx.txt'
        self.text += Controller.tools(path)

        hint = '提示：\n'
        hint += 'Buffer在不考慮能量的情況下，可以忽略\n'
        hint += 'Not, Not可以合併成Buffer\n'
        hint += 'And, Not可以合併成NAND\n'
        hint += 'Or, Not可以合併成NOR\n'
        hint += 'Xor, Not可以合併成XNOR\n'
        hint += 'NAND, Not可以合併成And\n'
        hint += 'NOR, Not可以合併成Or\n'
        hint += 'XNOR, Not可以合併成Xor\n'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
            'Scene': '8-1',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['parameters_game'] = {
            'question': {
                'response': '',
                'correct': '(答案正確)',
                'wrong': '(答案錯誤)',
                'answer': answer,
                'hint': hint,
                'solution': f'正確答案是：{answer}\n(Xor, NAND, Not, NOR, XNOR, NOR, Not, And)'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def scene_８_1(self):
        answer = '24'

        path = 'Model/Story/Level3/Scene7-ex.txt'
        self.text += Controller.tools(path)

        self.text += '\n(請輸入這8個邏輯閘的能量損耗加總)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '3',
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
                'hint': '出現什麼邏輯閘，就把上面對應的數字加總',
                'solution': f'正確答案是：{answer}\n(5 + 2 + 1 + 2 + 7 + 2 + 1 + 4)'
            },
            'config': {
                'chance': 5,
                'retry': 0
            }
        }

        return self.parameters, self.text

    def after_scene(self):
        path = 'Model/Story/Level3/AfterScene.txt'
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
            '7-1': self.scene_7_1,
            '8': self.scene_8,
            '8-1': self.scene_8_1,
            'after': self.after_scene
        }

        return scene[resp_scene]()