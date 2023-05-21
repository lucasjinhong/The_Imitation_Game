class CaesarCodec():
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encoder(self, plaintext, key):
        ciphertext = ''

        for char in plaintext:
            if char.isalpha():
                # 对于字母进行移位操作
                shifted_char = chr((ord(char.lower()) - ord('a') + key) % 26 + ord('a'))
            else:
                shifted_char = char
            ciphertext += shifted_char

        return ciphertext

    def decoder(self, ciphertext, key):
        plaintext = ''

        for char in ciphertext:
            if char.isalpha():
                # 对于字母进行移位操作
                shifted_char = chr((ord(char.lower()) - ord('a') - key + 26) % 26 + ord('a'))
            else:
                shifted_char = char
            plaintext += shifted_char

        return plaintext