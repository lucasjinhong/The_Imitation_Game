import random

class Level2Codec:
    def check_question_len(self, question, length):
        for _ in range(length - len(question)):
            question.append(format(random.randint(1,256), '08b'))

        return question

    def not_gate(self, question):
        question = self.check_question_len(question, 1)
        answer = ''
        
        for ans in question[0]:
            if ans == '0':
                answer += '1'
            else:
                answer += '0'

        return answer, question
    
    def and_gate(self, question):
        question = self.check_question_len(question, 2)
        answer = ''

        for i in range(len(question[0])):
            if question[0][i] == '1' and question[1][i] == '1':
                answer += '1'
            else:
                answer += '0'

        return answer, question
    
    def or_gate(self, question):
        question = self.check_question_len(question, 2)
        answer = ''

        for i in range(len(question[0])):
            if question[0][i] == '1' or question[1][i] == '1':
                answer += '1'
            else:
                answer += '0'

        return answer, question
    
    def xor_gate(self, question):
        question = self.check_question_len(question, 2)
        answer = ''

        for i in range(len(question[0])):
            if question[0][i] == question[1][i]:
                answer += '0'
            else:
                answer += '1'

        return answer, question
    
    def hex_to_bin(self, question):
        answer = []

        for _ in range(4):
            answer_nor = random.randint(1,256)
            question.append(format(answer_nor, '02x').upper())
            answer.append(format(answer_nor, '08b'))

        answer = ' '.join(answer)
        question = ' '.join(question)

        return answer, question

    def all_in_one(self, question):
        answer = [None]*4

        answer[0], _ = self.not_gate([question[0]])
        answer[1], _ = self.and_gate([question[1], answer[0]])
        answer[2], _ = self.or_gate([question[2], answer[1]])
        answer[3], _ = self.xor_gate([question[3], answer[2]])

        answer = ' '.join(answer)

        return answer

    def last_codec(self, question):
        answer = [None]*4

        answer[0], _ = self.xor_gate([question[0][0], question[1][0]])
        answer[1], _ = self.and_gate([question[0][1], question[1][1]])
        answer[2], _ = self.or_gate([question[0][2], question[1][2]])
        answer[3], _ = self.not_gate([question[0][3]])

        answer = ' '.join(answer)

        return answer

    def codec_handler(self, function, question):
        codec = {
            'not_gate': self.not_gate,
            'and_gate': self.and_gate,
            'or_gate': self.or_gate,
            'xor_gate': self.xor_gate,
            'hex_to_bin': self.hex_to_bin,
            'all_in_one': self.all_in_one,
            'last_codec': self.last_codec
        }

        return codec[function](question)