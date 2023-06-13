import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from View.Function.Story import Story
from View.WorkWidgets.Dialog import Dialog
from random import uniform
from View.Story.Level1 import Level1
from View.Story.Controller import Controller

class Main_Widget(QtWidgets.QWidget):
    back_window = QtCore.pyqtSignal()

    def __init__(self, username="you", story_index=1):
        super().__init__()
        self.setObjectName("main_widget")
        self.username = username
        self.story_index = story_index
        self.story = Story()
        self.typing = False
        self.paragraph_index = 0
        self.paragraph_to_type = []
        self.current_text = ''
        self.image_base_path = "View/Resource/Level1"
        self.setup_ui()
        self.execute()

        #init
        self.button_enter.setEnabled(False)
        self.parameters = {
            'function': 'scene_select',
            'parameters': {
                'Level': str(self.story_index),
                'Scene': '7',
                'last_question': '',
                'last_answer': '00000000 11111111 00000000 11111111'
            },
            'parameters_game': {
                'question': {
                    'response': '',
                    'correct': '',
                    'wrong': '',
                    'answer': '',
                    'hint': '',
                    'solution': ''
                },
                'config': {
                    'chance': 0,
                    'retry': 0
                }
            },
            'config': {
                'last_choose': '',
                'next_choose': '',
                'button_enter': True,
                'button_conti': True
            }
        }

    def setup_ui(self):
        self.setup_fonts()
        self.setup_timer()
        self.setup_buttons()
        self.setup_screen()
        self.setup_textEdit()
        self.setup_scrollArea()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setup_fonts(self):
        self.font_button = QtGui.QFont()
        self.font_button.setFamily("Arial")
        self.font_button.setPointSize(16)
        self.font_editor = QtGui.QFont()
        self.font_editor.setFamily("Arial")
        self.font_editor.setPointSize(20)

    def setup_timer(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_text)
        self.text_to_type = ''
        self.current_text = ''

    def setup_buttons(self):
        self.button_back = self.create_button(10, 445, 120, 35, "Button_Back", "回到主選單", self.button_back_click)
        self.button_help = self.create_button(830, 50, 100, 35, "Button_Help", "Help", self.button_help_click)
        self.button_conti = self.create_button(830, 330, 100, 35, "Button_Cont", "繼續", self.button_conti_click)
        self.button_enter = self.create_button(830, 395, 100, 35, "Button_Enter", "Enter", self.button_enter_click)

    def create_button(self, x, y, width, height, obj_name, text, slot_function):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(x, y, width, height))
        button.setFont(self.font_button)
        button.setObjectName(obj_name)
        button.setText(text)
        button.clicked.connect(slot_function)
        return button

    def setup_screen(self):
        self.screen = QtWidgets.QLabel(self)
        self.screen.setGeometry(QtCore.QRect(800, 100, 175, 200))
        self.screen.setFont(self.font_button)
        self.screen.setObjectName("Screen")
        self.screen.setText("I'm Screen")
        self.screen.setStyleSheet("border: 1px solid black;")

    def setup_textEdit(self):
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(120, 390, 661, 45))
        self.textEdit.setFont(self.font_editor)
        self.textEdit.setObjectName("textEdit")

        def clear_textEdit(event): # 讓點擊textEdit時，自動清除內容
            self.textEdit.clear()
            QtWidgets.QTextEdit.mousePressEvent(self.textEdit, event)

        self.textEdit.mousePressEvent = clear_textEdit

    def setup_scrollArea(self):
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(120, 40, 661, 321))
        self.scrollArea.setWidgetResizable(True)
        self.label = QtWidgets.QLabel(self)
        self.label.setFont(self.font_button)
        self.label.setText("")
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 311))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        self.scrollArea.setWidget(self.label)

    def execute(self):
        self.label.setText(f"{self.username} 你好，你選擇的是{self.story.get(self.story_index)}，請按「繼續」，開始你的冒險。")

    def button_back_click(self): # 加上確定要回到主選單嗎？
        confirm_box = QMessageBox()
        confirm_box.setIcon(QMessageBox.Question)
        confirm_box.setWindowTitle("確認")
        confirm_box.setText("確定要回到主選單嗎？(目前的遊玩進度將會消失)")
        confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_box.setDefaultButton(QMessageBox.No)
        reply = confirm_box.exec()

        if reply == QMessageBox.Yes:
            self.back_window.emit()

    def button_help_click(self): # TODO
        dlg = Dialog("測試: 測試", "此按鈕的功能仍在開發中")
        dlg.exec()

    def gate_select(self):
        gate = {
            '1': 'binary',
            '2': 'hexadecimal'
        }

        resp = self.textEdit.toPlainText()

        try:
            self.parameters['parameters']['Level'] = gate[resp]
            self.parameters['config']['last_choose'] = gate[resp]
            self.parameters['function'] = 'scene_select'
        except:
            text = '請選擇1或2'
        else:
            if resp == '1':
                self.parameters['config']['next_choose'] = gate['2']
            elif resp == '2':
                self.parameters['config']['next_choose'] = gate['1']

            text = f'你選擇的是{resp}\n'
            text += f'請點擊「繼續」鍵繼續'

            self.parameters['config']['button_enter'] = False
            self.parameters['config']['button_conti'] = True
            self.button_enter.setEnabled(self.parameters['config']['button_enter'])     #預防二次點擊
            self.button_conti.setEnabled(self.parameters['config']['button_conti'])

        self.paragraph_to_type.append(text)
        self.button_conti_click()

    def question_select(self):
        resp = self.textEdit.toPlainText().lower()
        self.parameters['parameters_game']['question']['response'] = resp

        self.parameters, text = Controller(self.parameters).question_select()

        self.button_enter.setEnabled(False)     #預防二次點擊
        self.button_conti.setEnabled(True)

        self.paragraph_to_type.append(text)
        self.button_conti_click()

    def button_enter_click(self):
        function = {
            'gate_select': self.gate_select,
            'scene_select': self.question_select
        }

        function[self.parameters['function']]()

    def button_conti_click(self):
        if self.typing and self.text_to_type:
            self.current_text += self.text_to_type
            self.text_to_type = ""
            self.typing = False

            if self.paragraph_index == len(self.paragraph_to_type) - 1:
                self.button_enter.setEnabled(self.parameters['config']['button_enter'])
                self.button_conti.setEnabled(self.parameters['config']['button_conti'])

            self.label.setText(self.current_text)
            QtCore.QTimer.singleShot(10, self.scroll_to_bottom)     # delay 10 毫秒到底部，讓點繼續時，也可以直接跳到最底部
        else:
            if self.paragraph_index >= len(self.paragraph_to_type) - 1:
                self.parameters, text = Controller(self.parameters).scene_select()
                self.paragraph_to_type += text.split("\n\n")

                if self.paragraph_index > 0:
                    self.paragraph_index += 1
            else:
                self.paragraph_index += 1

            self.text_to_type = self.paragraph_to_type[self.paragraph_index] + "\n\n"

            self.timer.start(100)
            self.typing = True

        image_path = os.path.join(self.image_base_path, f"img_{self.paragraph_index}.jpg")
        if os.path.exists(image_path):
            self.screen.setPixmap(QtGui.QPixmap(image_path))
            self.screen.setScaledContents(True)
        else:
            self.screen.clear()

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

            if self.paragraph_index == len(self.paragraph_to_type) - 1:
                self.button_enter.setEnabled(self.parameters['config']['button_enter'])
                self.button_conti.setEnabled(self.parameters['config']['button_conti'])

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