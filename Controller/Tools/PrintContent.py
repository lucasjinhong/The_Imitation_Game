import time
import random

class PrintContent:
    def __init__(self, path, skip) -> None:
        self.path = path
        self.skip = skip

    def execute(self):
        print()

        with open(self.path, encoding='utf8') as f:
            file_contents = f.read()

            if self.skip == 'y':
                print(file_contents)
            else:
                self.slow_type(file_contents)

    def slow_type(self, text):
        for i, char in enumerate(text):
            if char == '\n' and text[i - 1] == '\n':
                input('\n請點擊任意鍵繼續')

            print(char, end='', flush=True)
            typing_speed = random.uniform(0.01, 0.1)  # 生成0.01到0.1之间的随机等待时间
            time.sleep(typing_speed)