from Controller.Level.Game.Binary import Binary
from Controller.Level.Game.Hexadecimal import Hexadecimal
from Controller.Tools.PrintContent import PrintContent
import random

class Level1:
    def __init__(self, word):
        self.word = word
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

        self.skip = ''
        self.next_choose = 0
        self.gate = {
            1: Binary,
            2: Hexadecimal
        }

    def scene_1(self):
        path = 'Model\Story\Level1\Main\Scene1.txt'
        PrintContent(path, self.skip).execute()
        self.gate_select()

    def scene_2(self):
        path = 'Model\Story\Level1\Main\Scene2.txt'
        PrintContent(path, self.skip).execute()
        self.gate_select()

    def scene_3(self):
        path = 'Model\Story\Level1\Main\Scene3.txt'
        PrintContent(path, self.skip).execute()

        answer = 'future'
        question = self.future_codec(answer)
        print(f'它寫著：「{question}」，旁邊有一個讓你填的空白')
        print('你瞬間明白，這是一個謎題，')
        print('需要你結合之前「真實」和「虛幻」門後所學習到的知識，才能找到答案。\n')
        print('你默默地回想起自己在「真實」和「虛幻」路徑中遇到的各種挑戰和線索，')
        print('嘗試將這些信息組合起來，以解開這個謎題。')
        print('你明白，每個挑戰都讓你有所成長，而這最後的謎題將是你成長的總結。\n')

        for chance in range(5):
            if chance >= 3:
                print('提示：')
                print('1.結果會是6個英文字')
                print('2.英文數字對應表')
                print('--------------------------------------------------------------------------------')
                print('| a  b  c  d  e  f  g  f  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  s  y  z |')
                print('| 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 |')
                print('--------------------------------------------------------------------------------\n')

            res = input('請輸入要填上的文字：')

            if res == answer:
                print('恭喜你\n')
                break
            else:
                print('答案錯誤\n')

            if chance == 4:
                print(res)
                print(f'正確答案是：{answer}\n')

        return answer

    def after_scene(self, answer):
        print(f'當你將 {answer} 這個單詞填入空白處，')
        path = 'Model\Story\Level1\Main\AfterScene.txt'
        PrintContent(path, self.skip).execute()

    def future_codec(self, sentence):
        question = ''
        sentence = [ord(c) - 96 for c in sentence]

        for word in sentence:
            codec_type = random.randint(1, 2)

            if codec_type == 1:
                question += format(word, '08b') + ' '
            else:
                question += format(word, '04x') + ' '

        return question

    def gate_select(self):
        if self.next_choose > 0:
            print('爲了得到另一個門的知識，你自動選擇了與上次選擇相反的門。')
            input('\n點擊任意鍵開始下一關。')
            self.gate[self.next_choose](self.skip).execute()
        else:
            print('請選擇你第一個要走的門(倒數60秒)：')
            print('1.「真實」之門')
            print('2.「虛幻」之門')

            while True:
                try:
                    choose = int(input('\n請選擇：'))
                except:
                    print('Only for integer')
                    continue

                if choose == 1 or choose == 2:
                    if choose == 1:
                        self.next_choose = 2
                        path = 'Model\Story\Level1\Binary\GateSelectBinary.txt'
                        PrintContent(path, self.skip).execute()
                    else:
                        self.next_choose = 1
                        path = 'Model\Story\Level1\Hexadecimal\GateSelectHexadecimal.txt'
                        PrintContent(path, self.skip).execute()

                    self.gate[choose](self.skip).execute()
                    break
                else:
                    print('Unknown Choose')

    def execute(self):
        while True:
            self.skip = input('是否加速劇情？(y/n):')
            if self.skip == 'y' or self.skip == 'n':
                break

        self.scene_1()
        self.scene_2()
        answer = self.scene_3()
        self.after_scene(answer)