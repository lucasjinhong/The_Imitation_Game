from Codec.XorCodec import XorCodec
from Controller.printSolve import printSolve

class Xor():
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

    def execute(self, word):
        ciphertext = XorCodec().encoder(word, self.key)
        plaintext = XorCodec().decoder(ciphertext, self.key)
        printSolve.print_cipher_and_solve('Xor', ciphertext, plaintext)