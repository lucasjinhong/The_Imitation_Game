class SubstitutionCodec():
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encoder(self, plaintext, key):
        ciphertext = ''

        for char in plaintext.upper():
            if char in self.alphabet:
                index = self.alphabet.index(char)
                ciphertext += key[index]
            else:
                ciphertext += char

        return ciphertext

    def decoder(self, ciphertext, key):
        plaintext = ''

        for char in ciphertext.upper():
            if char in key:
                index = key.index(char)
                plaintext += self.alphabet[index]
            else:
                plaintext += char

        return plaintext