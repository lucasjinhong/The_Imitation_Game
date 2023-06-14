import random

class Level1Codec:
    def dec_to_bin(self):
        answer_dec = random.randint(1,256)
        answer_bin = format(answer_dec, '08b')

        return answer_dec, answer_bin

    def bin_to_dec(self):
        answer_dec = random.randint(1,256)
        answer_bin = format(answer_dec, '08b')

        return answer_bin, answer_dec
    
    def dec_to_hex(self):
        answer_dec = random.randint(1,65535)
        answer_hex = format(answer_dec, '04x')

        return answer_dec, answer_hex

    def hex_to_dec(self):
        answer_dec = random.randint(1,65535)
        answer_hex = format(answer_dec, '04x')

        return answer_hex, answer_dec
    
    def future_codec(self):
        answer = 'future'
        question = ''
        sentence = [ord(c) - 96 for c in answer]

        for word in sentence:
            codec_type = random.randint(1, 2)

            if codec_type == 1:
                question += format(word, '08b') + ' '
            else:
                question += format(word, '04x') + ' '

        return answer, question
    
    def codec_handler(self, function, answer_last):
        codec = {
            'dec_to_bin': self.dec_to_bin,
            'bin_to_dec': self.bin_to_dec,
            'dec_to_hex': self.dec_to_hex,
            'hex_to_dec': self.hex_to_dec,
            'future_codec': self.future_codec
        }

        return codec[function]()