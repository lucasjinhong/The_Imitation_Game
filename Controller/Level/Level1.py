from Controller.Level.Game.Binary import Binary
from Controller.Level.Game.Hexadecimal import Hexadecimal

class Level1:
    def __init__(self, word):
        self.word = word
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

        self.gate = {
            1: Binary,
            2: Hexadecimal,
        }

    def scene_1(self):
        with open('Model\Story\Level1\Main\Scene1.txt', encoding='utf8') as f:
            file_contents = f.read()
            print (file_contents)
        self.gate_select()

    def scene_2(self):
        with open('Model\Story\Level1\Main\Scene2.txt', encoding='utf8') as f:
            file_contents = f.read()
            print (file_contents)
        self.gate_select()

    def scene_3(self):
        with open('Model\Story\Level1\Main\Scene3.txt', encoding='utf8') as f:
            file_contents = f.read()
            print (file_contents)

    def gate_select(self):
        print('請選擇你第一個要走的門(倒數60秒)：')
        print('1.「真實」之門')
        print('2.「虛幻」之門')

        while True:
            try:
                choose = int(input('\n請選擇：'))
            except:
                print('Only for integer')
                pass

            if choose == 1 or choose == 2:
                if choose == 1:
                    with open('Model\Story\Level1\Binary\GateSelectBinary.txt', encoding='utf8') as f:
                        file_contents = f.read()
                        print (file_contents)
                else:
                    with open('Model\Story\Level1\Hexadecimal\GateSelectHexadecimal.txt', encoding='utf8') as f:
                        file_contents = f.read()
                        print (file_contents)

                self.gate[choose]().execute()
                break
            else:
                print('Unknown Choose')

    def execute(self):
        self.scene_1()
        self.scene_2()
        # self.scene_3()

        # ciphertext = SubstitutionCodec().encoder(self.word, self.key)
        # plaintext = SubstitutionCodec().decoder(ciphertext, self.key)
        # printSolve.print_cipher_and_solve('Substitution', ciphertext, plaintext)