import random

class Level2Codec:
    def nor_to_not(_):
        answer_nor = random.randint(1,256)
        answer_bin = format(answer_nor, '08b')
        answer_not = ''
        
        for ans in answer_bin:
            if ans == '0':
                answer_not += '1'
            else:
                answer_not += '0'

        return answer_bin, answer_not
    
    def nor_and_not(answer_not):
        answer_nor = random.randint(1,256)
        answer_bin = format(answer_nor, '08b')
        answer_and = ''
        
        ans_b = answer_bin.strip()
        ans_n = answer_not.strip()

        for i in range(len(answer_bin)):
            if ans_b[i] == '1' and ans_n[i] == '1':
                answer_and += '1'
            else:
                answer_and += '0'

        return answer_bin, answer_and
    
    def nor_or_and(answer_and):
        answer_nor = random.randint(1,256)
        answer_bin = format(answer_nor, '08b')
        answer_or = ''

        ans_b = answer_bin.strip()
        ans_a = answer_and.strip()

        for i in range(len(answer_bin)):
            if ans_b[i] == '1' or ans_a[i] == '1':
                answer_or += '1'
            else:
                answer_or += '0'

        return answer_bin, answer_or
    
    def nor_xor_or(answer_or):
        answer_nor = random.randint(1,256)
        answer_bin = format(answer_nor, '08b')
        answer_xor = ''

        ans_b = answer_bin.strip()
        ans_o = answer_or.strip()

        for i in range(len(answer_bin)):
            if ans_b[i] == ans_o[i]:
                answer_xor += '0'
            else:
                answer_xor += '1'

        return answer_bin, answer_xor
    
    def hex_to_bin(_):
        answer_hex = []
        answer_bin = []

        for _ in range(4):
            answer_nor = random.randint(1,256)
            answer_hex.append(format(answer_nor, '04x'))
            answer_bin.append(format(answer_nor, '08b'))

        answer_bin = ' '.join(answer_bin)
        answer_hex = ' '.join(answer_hex)

        return answer_hex, answer_bin

    def all_in_one(answer_bin):
        answer_not = ''
        answer_and = ''
        answer_or = ''
        answer_xor = ''
        answer_all = []

        for ans in answer_bin[0]:
            if ans == '0':
                answer_not += '1'
            else:
                answer_not += '0'

        answer_all.append(answer_not)

        ans_b = answer_bin[1].strip()
        ans_n = answer_not.strip()

        for i in range(len(ans_b)):
            if ans_b[i] == '1' and ans_n[i] == '1':
                answer_and += '1'
            else:
                answer_and += '0'

        answer_all.append(answer_and)

        ans_b = answer_bin[2].strip()
        ans_a = answer_and.strip()

        for i in range(len(ans_b)):
            if ans_b[i] == '1' or ans_a[i] == '1':
                answer_or += '1'
            else:
                answer_or += '0'

        answer_all.append(answer_or)

        ans_b = answer_bin[3].strip()
        ans_o = answer_or.strip()

        for i in range(len(ans_b)):
            if ans_b[i] == ans_o[i]:
                answer_xor += '0'
            else:
                answer_xor += '1'

        answer_all.append(answer_xor)
        answer_all = ' '.join(answer_all)

        return answer_all