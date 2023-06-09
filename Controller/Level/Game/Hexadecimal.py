from Controller.Tools.PrintContent import PrintContent
import random

class Hexadecimal:
    def __init__(self, skip):
        self.skip = skip

    def before_scene(self):
        path = 'Model\Story\Level1\Hexadecimal\BeforeScene.txt'
        PrintContent(path, self.skip).execute()

    def question_1(self):
        answer = random.randint(1,65535)
        answer_hex = format(answer, '04x')

        print('[第一關]')
        print(f'若一串十六進制數字為{answer_hex}，它代表的十進制數字是多少？\n')

        for chance in range(5):
            if chance >= 3:
                print('提示：每位數的十六進制數字都對應到一個0至15的十進制數字，並且每向左移一位，其值就增加16倍。')

            res = input('請輸入你的答案:')

            if res == str(answer):
                print('恭喜你\n')
                break
            else:
                print('答案錯誤\n')

            if chance == 4:
                print(f'正確答案是：{answer}\n')

        print('顯示板上又出現了一個更複雜的問題。\n')

    def question_2(self):
        answer = random.randint(1,256)
        answer_bin = format(answer, '04x')

        print('[第二關]')
        print(f'若一串十進制數字為{answer}，它代表的十六進制數字是多少？\n')

        for chance in range(5):
            if chance >= 3:
                print('提示：反覆除以16，看餘數，並反向排列所有的餘數')

            res = input('請輸入你的答案:')

            if res == str(answer_bin):
                print('恭喜你\n')
                break
            else:
                print('答案錯誤\n')

            if chance == 4:
                print(res)
                print(f'正確答案是：{answer_bin}\n')

        print('你覺得應該結束了，十六進制應該就這樣了，')
        print('把十六進制轉成十進制，把十進制轉成十六進制，')
        print('最重要的應該就是這兩個觀念，')
        print('但這時，螢幕上出現了第三題：\n')

    def question_3(self):
        retry = 0
        print('[第三關]')
        print('請問 1 + 1 = ？\n')

        for chance in range(3):
            res = input('你心想，這個問題這麼簡單，毫不猶豫的輸入答案：')

            if res == '2':
                print('機器人：「你很勇嘛。」\n')
                break
            else:
                print('機器人：「答案錯誤。」\n')

            if chance == 2:
                print('機器人：「我看你是完全不懂喔。」')
                print('機器人：「從第一關開始吧。」\n')
                retry = 1

        return retry

    def after_scene(self):
        path = 'Model\Story\Level1\Hexadecimal\AfterScene.txt'
        PrintContent(path, self.skip).execute()

    def execute(self):
        self.before_scene()

        while True:
            self.question_1()
            self.question_2()
            retry = self.question_3()

            if retry == 0:
                break

        self.after_scene()