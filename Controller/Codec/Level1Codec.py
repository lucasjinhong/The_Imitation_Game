import random

class Level1Codec:
    def dec_to_bin(self, question):
        question.append(random.randint(1,256))
        answer = format(question[0], '08b')

        return answer, question

    def bin_to_dec(self, question):
        question.append(random.randint(1,256))
        answer = format(question[0], '08b')

        return answer, question

    def dec_to_hex(self, question):
        question.append(random.randint(1,65535))
        answer = format(question[0], '04x')

        return answer, question

    def hex_to_dec(self, question):
        question.append(random.randint(1,65535))
        answer = format(question[0], '04x')

        return answer, question

    def future_codec(self, question):
        answer = 'future'
        question_temp = []
        sentence = [ord(c) - 96 for c in answer]

        for word in sentence:
            codec_type = random.randint(1, 2)

            if codec_type == 1:
                question_temp.append(format(word, '08b'))
            else:
                question_temp.append(format(word, '04x').upper())

        question.append(' '.join(question_temp))

        return answer, question

    def codec_handler(self, function, question):
        codec = {
            'dec_to_bin': self.dec_to_bin,
            'bin_to_dec': self.bin_to_dec,
            'dec_to_hex': self.dec_to_hex,
            'hex_to_dec': self.hex_to_dec,
            'future_codec': self.future_codec
        }

        return codec[function](question)