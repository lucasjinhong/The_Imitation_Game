import random

class BinaryCodec:
    def dec_to_bin():
        answer_dec = random.randint(1,256)
        answer_bin= format(answer_dec, '08b')

        return answer_dec, answer_bin

    def bin_to_dec():
        answer_dec = random.randint(1,256)
        answer_bin= format(answer_dec, '08b')

        return answer_bin, answer_dec