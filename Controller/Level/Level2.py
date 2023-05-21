from Controller.Codec.AtbashCodec import AtbashCodec
from Controller.Tools.printSolve import printSolve

class Level2:
    def __init__(self, word):
        self.word = word
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = self.alphabet[::-1]

    def execute(self):
        print()
        print('明文字母表：' + self.alphabet)
        print('密文字母表：' + self.key)
        print()

        ciphertext = AtbashCodec().encoder(self.word, self.key)
        plaintext = AtbashCodec().decoder(ciphertext, self.key)
        printSolve.print_cipher_and_solve('Atbash', ciphertext, plaintext)