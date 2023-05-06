from Codec.SubstitutionCodec import SubstitutionCodec
from Controller.printSolve import printSolve

class Substitution():
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

    def execute(self, word):
        print()
        print('明文字母表：' + self.alphabet)
        print('密文字母表：' + self.key)
        print()

        ciphertext = SubstitutionCodec().encoder(word, self.key)
        plaintext = SubstitutionCodec().decoder(ciphertext, self.key)
        printSolve.print_cipher_and_solve('Substitution', ciphertext, plaintext)