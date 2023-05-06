from Codec.AtbashCodec import AtbashCodec
from Controller.printSolve import printSolve

class Atbash():
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = self.alphabet[::-1]

    def execute(self, word):
        print()
        print('明文字母表：' + self.alphabet)
        print('密文字母表：' + self.key)
        print()

        ciphertext = AtbashCodec().encoder(word, self.key)
        plaintext = AtbashCodec().decoder(ciphertext, self.key)
        printSolve.print_cipher_and_solve('Atbash', ciphertext, plaintext)