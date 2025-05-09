from Controller.Controller import Controller
from View.Story.Game.Binary import Binary
from View.Story.Game.Hexadecimal import Hexadecimal

class Level1:
    def __init__(self, parameters):
        self.parameters = parameters
        self.text = ''
        self.next_choose = parameters['config']['next_choose']

        self.gate = {
            '1': Binary,
            '2': Hexadecimal
        }

    def scene_1(self):
        path = 'Model/Story/Level1/Main/Scene1.txt'
        self.text += Controller.tools(path)

        self.text += '\n請選擇你第一個要走的門(倒數60秒)：\n'
        self.text += '1.「真實」之門\n'
        self.text += '2.「虛幻」之門\n'
        self.text += '(請輸入數字1或2)'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'gate_select'
        self.parameters['parameters'] = {
            'Level': '',
            'Scene': 'before',
            'last_question': '',
            'last_answer': ''
        }

        return self.parameters, self.text

    def scene_2(self):
        gate = {
            'binary': '「真實」之門',
            'hexadecimal': '「虛幻」之門'
        }
        last_choose = gate[self.parameters['config']['last_choose']]
        next_choose = gate[self.parameters['config']['next_choose']]

        path = 'Model/Story/Level1/Main/Scene2.txt'
        self.text += Controller.tools(path)

        self.text += '\n你再次站在那兩扇門前，那種強烈的熟悉感湧上心頭\n'
        self.text += f'你回憶起剛剛選擇{last_choose}後所經歷的一切，\n'
        self.text += '一個充滿未知的路程，最後卻落得空空如也的結果。\n'
        self.text += '然而，你並沒有因此感到失望或者懊惱，\n'
        self.text += '反而，你感到了一股無法形容的決心。\n\n'

        self.text += f'你再次看向那兩扇門，然後毫不猶豫地選擇了{next_choose}。\n'
        self.text += '當你走向那扇門時，你感到了一股奇特的能量，\n'
        self.text += '它似乎在引導你，告訴你這一次的選擇將會有所不同。'

        self.parameters['config']['button_enter'] = False
        self.parameters['config']['button_conti'] = True

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': self.next_choose,
            'Scene': 'before',
            'last_question': '',
            'last_answer': ''
        }
        self.parameters['config']['next_choose'] = ''

        return self.parameters, self.text

    def scene_3(self):
        answer, question = Controller.codec('1', 'future_codec')

        path = 'Model/Story/Level1/Main/Scene3.txt'
        self.text += Controller.tools(path)

        self.text +=f'它寫著：「{question[0]}」，旁邊有一個讓你填的空白\n'
        self.text +='你瞬間明白，這是一個謎題，\n'
        self.text +='需要你結合之前「真實」和「虛幻」門後所學習到的知識，才能找到答案。\n\n'

        self.text +='你默默地回想起自己在「真實」和「虛幻」路徑中遇到的各種挑戰和線索，\n'
        self.text +='嘗試將這些信息組合起來，以解開這個謎題。\n'
        self.text +='你明白，每個挑戰都讓你有所成長，而這最後的謎題將是你成長的總結。\n\n'
        self.text +='(請輸入6個英文字母，用已知的知識來解題)'

        hint = '提示：\n'
        hint += '1. 結果會是6個英文字\n'
        hint += '2. 英文數字對應表\n'
        hint += '｜－　－　－　－　－　－　－　－　－　－　－　－　－｜\n\n'
        hint += '　ａ　ｂ　ｃ　ｄ　ｅ　ｆ　ｇ　ｈ　ｉ\n'
        hint += '　１　２　３　４　５　６　７　８　９\n\n'
        hint += '　ｊ　　ｋ　　ｌ　　ｍ　　ｎ　　ｏ　　ｐ　　ｑ\n'
        hint += '　１０　１１　１２　１３　１４　１５　１６　１７\n\n'
        hint += '　ｒ　　ｓ　　ｔ　　ｕ　　ｖ　　ｗ　　ｘ　　ｙ　　ｚ\n'
        hint += '　１８　１９　２０　２１　２２　２３　２４　２５　２６\n\n'
        hint += '　－　　－　　－　　－　　－　　－　　－　　－　　－｜\n'

        self.parameters['config']['button_enter'] = True
        self.parameters['config']['button_conti'] = False

        self.parameters['function'] = 'scene_select'
        self.parameters['parameters'] = {
            'Level': '1',
            'Scene': 'after',
            'last_question': '',
            'last_answer': answer
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

    def after_scene(self):
        last_answer = self.parameters['parameters']['last_answer']

        self.text += f'當你將 {last_answer} 這個單詞填入空白處，\n'

        path = 'Model/Story/Level1/Main/AfterScene.txt'
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
            'after': self.after_scene
        }

        return scene[resp_scene]()