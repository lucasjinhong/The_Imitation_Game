import random

class Level2Codec:
    def not_gate(self, answer_bin, answer_last=''):
        answer_not = ''
        
        for ans in answer_bin:
            if ans == '0':
                answer_not += '1'
            else:
                answer_not += '0'

        return answer_not, answer_bin 
    
    def and_gate(self, answer_bin, answer_last=''):
        answer_and = ''

        ans_a = answer_last.strip()
        ans_b = answer_bin.strip()
        ans_len = len(answer_bin)

        for i in range(ans_len):
            if ans_b[i] == '1' and ans_a[i] == '1':
                answer_and += '1'
            else:
                answer_and += '0'

        return answer_and, answer_bin
    
    def or_gate(self, answer_bin, answer_last=''):
        answer_or = ''

        ans_a = answer_last.strip()
        ans_b = answer_bin.strip()
        ans_len = len(answer_bin)

        for i in range(ans_len):
            if ans_b[i] == '1' or ans_a[i] == '1':
                answer_or += '1'
            else:
                answer_or += '0'

        return answer_or, answer_bin
    
    def xor_gate(self, answer_bin, answer_last=''):
        answer_xor = ''

        ans_a = answer_last.strip()
        ans_b = answer_bin.strip()
        ans_len = len(answer_bin)

        for i in range(ans_len):
            if ans_b[i] == ans_a[i]:
                answer_xor += '0'
            else:
                answer_xor += '1'

        return  answer_xor, answer_bin
    
    def hex_to_bin(self, answer_bin, answer_last=''):
        answer_hex = []
        answer_bin = []

        for _ in range(4):
            answer_nor = random.randint(1,256)
            answer_hex.append(format(answer_nor, '02x').upper())
            answer_bin.append(format(answer_nor, '08b'))

        answer_bin = ' '.join(answer_bin)
        answer_hex = ' '.join(answer_hex)

        return answer_hex, answer_bin

    def all_in_one(self, answer_bin, answer_last=''):
        answer = [None]*4

        answer[0], _ = self.not_gate(answer_last[0])
        answer[1], _ = self.and_gate(answer_last[1], answer[0])
        answer[2], _ = self.or_gate(answer_last[2], answer[1])
        answer[3], _ = self.xor_gate(answer_last[3], answer[2])

        answer = ' '.join(answer)

        return answer
    
    def last_codec(self, answer_bin, answer_last=''):
        answer = [None]*4

        answer[0], _ = self.xor_gate(answer_last[1], answer_last[0])
        answer[1], _ = self.and_gate(answer_last[2], answer[0])
        answer[2], _ = self.or_gate(answer_last[3], answer[1])
        answer[3], _ = self.not_gate(answer[2])

        answer = ' '.join(answer)

        return answer
    
    def codec_handler(self, function, answer_last):
        answer_bin = format(random.randint(1,256), '08b')

        codec = {
            'not_gate': self.not_gate,
            'and_gate': self.and_gate,
            'or_gate': self.or_gate,
            'xor_gate': self.xor_gate,
            'hex_to_bin': self.hex_to_bin,
            'all_in_one': self.all_in_one,
            'last_codec': self.last_codec
        }

        return codec[function](answer_bin, answer_last)