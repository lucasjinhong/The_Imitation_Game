from collections import Counter
import string

with open('en_article.txt', 'r') as file:
    data = file.read()

# 過濾掉標點符號
translator = str.maketrans('', '', string.punctuation)
data = data.translate(translator)

# 創建單詞列表
words = data.split()
words = [word.lower() for word in words if word.isalpha()]

# 計算單詞出現頻率
word_counts = Counter(words)

# 找到出現頻率最高的單詞
most_common_words = word_counts.most_common(20)

for word, count in most_common_words:
    print(f'{word}: {count}')

# 寫入結果到新的檔案
with open('20_most_common_word.txt', 'w') as file:
    for word, count in most_common_words:
        file.write(f'{word}\n')
