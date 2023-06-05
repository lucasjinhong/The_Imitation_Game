if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from PyQt5 import QtCore, QtGui, QtWidgets
from Function.Story import Story
from WorkWidgets.Dialog import Dialog
from random import uniform


class Main_Widget(QtWidgets.QWidget):
    back_window = QtCore.pyqtSignal()

    def __init__(self, username="you", story_index=1):
        super().__init__()
        self.setObjectName("ui_3")
        self.username = username
        self.story_index = story_index
        self.story = Story()
        self.typing = False
        self.paragraph_index = 0
        self.current_text = ''

        # Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_text)
        self.text_to_type = ""
        self.current_text = ""

        font_16 = QtGui.QFont()
        font_16.setFamily("Arial")
        font_16.setPointSize(16)
        font_20 = QtGui.QFont()
        font_20.setFamily("Arial")
        font_20.setPointSize(20)

        self.button_back = QtWidgets.QPushButton(self)
        self.button_back.setGeometry(QtCore.QRect(10, 445, 120, 35))
        self.button_back.setFont(font_16)
        self.button_back.setObjectName("Button_Back")
        self.button_back.setText("回到主選單")
        self.button_back.clicked.connect(self.button_back_click)

        self.button_enter = QtWidgets.QPushButton(self)
        self.button_enter.setGeometry(QtCore.QRect(830, 395, 100, 35))
        self.button_enter.setFont(font_16)
        self.button_enter.setObjectName("Button_Enter")
        self.button_enter.setText("Enter")
        self.button_enter.clicked.connect(self.button_enter_click)

        self.button_coti = QtWidgets.QPushButton(self)
        self.button_coti.setGeometry(QtCore.QRect(830, 330, 100, 35))
        self.button_coti.setFont(font_16)
        self.button_coti.setObjectName("Button_Cont")
        self.button_coti.setText("繼續")
        self.button_coti.clicked.connect(self.button_coti_click)

        self.button_help = QtWidgets.QPushButton(self)
        self.button_help.setGeometry(QtCore.QRect(830, 50, 100, 35))
        self.button_help.setFont(font_16)
        self.button_help.setObjectName("Button_Help")
        self.button_help.setText("Help")
        self.button_help.clicked.connect(self.button_help_click)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(120, 390, 661, 45))
        self.textEdit.setFont(font_20)
        self.textEdit.setObjectName("textEdit")

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(120, 40, 661, 321))
        self.scrollArea.setWidgetResizable(True)
        self.label = QtWidgets.QLabel(self)
        self.label.setFont(font_16)
        self.label.setText("")
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 311))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        self.scrollArea.setWidget(self.label)

        QtCore.QMetaObject.connectSlotsByName(self)

        #測試
        self.execute()

    def execute(self):
        self.label.setText(f"{self.username} 你好，你選擇的是{self.story.get(self.story_index)}，請按繼續，開始你的冒險。")

    def button_back_click(self):
        self.back_window.emit()

    def button_help_click(self):
        dlg = Dialog("測試: 非霖不投", "為什麼你要點這個按鈕呢???")
        dlg.exec()

    def button_enter_click(self):
        self.textEdit.setText('')

    def button_coti_click(self):
        if self.typing and self.text_to_type:  # 確保 self.text_to_type 不為空
            self.current_text += self.text_to_type
            self.text_to_type = ""
            self.label.setText(self.current_text)
            self.typing = False
            QtCore.QTimer.singleShot(10, self.scroll_to_bottom)  # delay 10 毫秒到底部，讓點繼續時，也可以直接跳到最底部
        else:
            with open('Scene1_test.txt', 'r', encoding='utf-8') as f:
                self.story_text = f.read()
            self.paragraphs_to_type = self.story_text.split("\n\n")
            if self.paragraph_index < len(self.paragraphs_to_type):
                self.text_to_type = self.paragraphs_to_type[self.paragraph_index] + "\n\n"
                self.paragraph_index += 1
            else:
                self.text_to_type = ""
            self.timer.start(100)
            self.typing = True

    def update_text(self):
        if self.text_to_type:
            self.current_text += self.text_to_type[0]
            self.text_to_type = self.text_to_type[1:]
            self.label.setText(self.current_text)
            self.timer.setInterval(int(uniform(10, 100)))  # 10到100毫秒之間的隨機等待時間

            # 讓文字在顯示時，滾動區域一起滾動到底部
            scrollbar = self.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
        else:
            self.timer.stop()
            self.typing = False


    def scroll_to_bottom(self):
        # 讓點下「繼續」時，滾動區域「也」可以滾動到底部
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_Widget()
    main_window.setFixedSize(1000, 500)
    main_window.show()
    sys.exit(app.exec_())
