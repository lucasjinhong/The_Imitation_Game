import random
import nltk

class Random():
    def __init__(self):
        pass

    def random_word(self):
        # 获取长度为word_length的单词列表

        with open('Text\en\most_common_word.txt', 'r') as file:
            words = file.read().splitlines()

        # 随机生成一个有意义的英文单词
        word = random.choice(words)

        return word