import random

class FutureCodec:
    def future_codec():
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