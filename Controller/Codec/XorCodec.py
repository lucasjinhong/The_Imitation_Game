class XorCodec():
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encoder(self, plaintext, key):
        ciphertext = ''

        for i in range(len(plaintext)):
            # 对于每个字符和密钥进行异或操作
            shifted_char = chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
            ciphertext += shifted_char

        return ciphertext

    def decoder(self, ciphertext, key):
        plaintext = ''

        for i in range(len(ciphertext)):
            # 对于每个字符和密钥进行异或操作
            shifted_char = chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
            plaintext += shifted_char

        return plaintext