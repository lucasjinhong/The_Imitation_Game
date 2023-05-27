import random

class Binary:
    def __init__(self):
        pass

    def before_scene(self):
        with open('Model\Story\Level1\Binary\BeforeScene.txt', encoding='utf8') as f:
            file_contents = f.read()
            print (file_contents)

    def question_1(self):
        answer = random.randint(1,256)
        answer_bin = format(answer, '08b')

        print('[第一關]')
        print(f'若一串二進制數字為{answer_bin}，它代表的十進制數字是多少？\n')
        
        for chance in range(5):
            if chance >= 3:
                print('hint：每左移一個數字，就是前一個數字的兩倍')

            res = input('請輸入你的答案:')

            if res == str(answer):
                print('恭喜你\n')
                break
            else:
                print('答案錯誤\n')

            if chance == 4:
                print(f'正確答案是：{answer}\n')

        print('這時，螢幕上又繼續顯示了下一題。')

    def question_2(self):
        answer = random.randint(1,256)
        answer_bin = format(answer, '08b')
        
        print('[第二關]')
        print(f'若一串十進制數字為{answer}，它代表的二進制數字是多少？\n')
        
        for chance in range(5):
            if chance >= 3:
                print('hint：反覆除以2，看餘數，並反向排列所有的餘數')

            res = input('請輸入你的答案:')

            if res == str(answer_bin):
                print('恭喜你\n')
                break
            else:
                print('答案錯誤\n')

            if chance == 4:
                print(res)
                print(f'正確答案是：{answer_bin}\n')

        print('''你覺得應該結束了，二進制應該就這樣了，
              \n把二進制轉成十進制，把十進制轉成二進制，
              \n最重要的應該就是這兩個觀念，
              \n但這時，螢幕上出現了第三題：''')

    def question_3(self):
        retry = 0
        print('[第三關]')
        print('請問 1 + 1 = ？\n')

        for chance in range(5):
            res = input('你心想，這個問題這麼簡單，毫不猶豫的輸入答案：')

            if res == '10':
                print('機器人：「你很勇嘛。」\n')
                break
            else:
                print('機器人：「答案錯誤。」\n')

            if chance == 4:
                print('機器人：「我看你是完全不懂喔。」')
                print('機器人：「從第一關開始吧。」\n')
                retry = 1

        return retry

    def after_scene(self):
        with open('Model\Story\Level1\Binary\AfterScene.txt', encoding='utf8') as f:
            file_contents = f.read()
            print (file_contents)

    def execute(self):
        self.before_scene()

        while True:
            self.question_1()
            self.question_2()
            retry = self.question_3()

            if retry == 0:
                break

        self.after_scene()