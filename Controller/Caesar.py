from Codec.CaesarCodec import CaesarCodec
from Controller.printSolve import printSolve
import random

class Caesar():
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.end = 3
        self.key = ''

    def random_shift(self, end):
        shift = random.randint(1, end)

        return shift

    def execute(self, word):
        self.key = int(random.randint(1, self.end))

        ciphertext = CaesarCodec().encoder(word, self.key)
        plaintext = CaesarCodec().decoder(ciphertext, self.key)
        printSolve.print_cipher_and_solve('Caesar', ciphertext, plaintext)