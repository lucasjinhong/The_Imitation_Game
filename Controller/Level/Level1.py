from Controller.Codec.SubstitutionCodec import SubstitutionCodec
from Controller.Tools.printSolve import printSolve

class Level1:
    def __init__(self, word):
        self.word = word
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

    def execute(self):
        print()
        print('明文字母表：' + self.alphabet)
        print('密文字母表：' + self.key)
        print()

        ciphertext = SubstitutionCodec().encoder(self.word, self.key)
        plaintext = SubstitutionCodec().decoder(ciphertext, self.key)
        printSolve.print_cipher_and_solve('Substitution', ciphertext, plaintext)