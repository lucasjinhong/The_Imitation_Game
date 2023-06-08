# from Controller.Codec.CaesarCodec import CaesarCodec
# from Controller.Tools.printSolve import printSolve
# import random

# class Level3:
#     def __init__(self, word):
#         self.word = word
#         self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         self.key = 0
#         self.end = 3

#     def execute(self):
#         self.key = int(random.randint(1, self.end))

#         print()
#         print('明文字母表：' + self.alphabet)
#         print('密文字母表：' + str(self.key))
#         print()

#         ciphertext = CaesarCodec().encoder(self.word, self.key)
#         plaintext = CaesarCodec().decoder(ciphertext, self.key)
#         printSolve.print_cipher_and_solve('Caesar', ciphertext, plaintext)