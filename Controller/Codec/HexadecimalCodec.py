import random

class HexadecimalCodec:
    def dec_to_hex():
        answer_dec = random.randint(1,65535)
        answer_hex= format(answer_dec, '04x')

        return answer_dec, answer_hex

    def hex_to_dec():
        answer_dec = random.randint(1,65535)
        answer_hex= format(answer_dec, '04x')

        return answer_hex, answer_dec