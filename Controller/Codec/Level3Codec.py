import random
from Controller.Codec.Level2Codec import Level2Codec

class Level3Codec:
    def check_question_len(self, question, length):
        for _ in range(length - len(question)):
            question.append(format(random.randint(1,256), '08b'))

        return question

    def majority_vote(self, question):
        question = self.check_question_len(question, 5)
        answer = ''
        
        for i in range(8):
            sum_of_bin = {
                '0': 0,
                '1': 0
            }
        
            for j in range(5):
                sum_of_bin[question[j][i]] += 1

            if sum_of_bin['0'] > sum_of_bin['1']:
                answer += '0'
            else:
                answer += '1'

        return answer, question
    
    def nand_gate(self, question):
        question = self.check_question_len(question, 2)
        answer = ''

        for i in range(8):
            if question[0][i] == '1' and question[1][i] == '1':
                answer += '0'
            else:
                answer += '1'

        return answer, question
    
    def nor_gate(self, question):
        question = self.check_question_len(question, 2)
        answer = ''

        for i in range(8):
            if question[0][i] == '1' or question[1][i] == '1':
                answer += '0'
            else:
                answer += '1'

        return answer, question
    
    def xnor_gate(self, question):
        question = self.check_question_len(question, 2)
        answer = ''

        for i in range(len(question[0])):
            if question[0][i] == question[1][i]:
                answer += '1'
            else:
                answer += '0'

        return answer, question
    
    def xor_xnor_gate(self, question):
        question = self.check_question_len(question, 5)
        answer = [None]*4

        answer[0], _ = Level2Codec().xor_gate([question[0], question[1]])
        answer[1], _ = self.xnor_gate([question[2], answer[0]])
        answer[2], _ = Level2Codec().xor_gate([question[3], answer[1]])
        answer[3], _ = self.xnor_gate([question[4], answer[2]])

        answer = ' '.join(answer)

        return answer, question
    
    def buffer_gate(self, question):
        random_numbers = random.sample(2 * list(range(1,5)), 8)
        question_temp = ''
        answer = ''
        energy = 6

        alphabet = {
            1: 'T',
            2: 'O',
            3: 'N',
            4: 'X'
        }

        for alphabet_energy in random_numbers:
            if energy <= alphabet_energy:
                answer += 'B'
                energy += 6
            
            question_temp += alphabet[alphabet_energy]
            answer += alphabet[alphabet_energy]
            energy -= alphabet_energy

        question.append(''.join(question_temp))

        return answer, question

    def codec_handler(self, function, question):
        codec = {
            'majority_vote': self.majority_vote,
            'nand_gate': self.nand_gate,
            'nor_gate': self.nor_gate,
            'xor_xnor_gate': self.xor_xnor_gate,
            'buffer_gate': self.buffer_gate
        }

        return codec[function](question)