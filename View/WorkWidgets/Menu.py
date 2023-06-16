
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from View.Function.Story import Story

class Menu(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(int) # 換到Main_Widget要用的
    back_window = QtCore.pyqtSignal() # 回到Login要用的

    def __init__(self):
        super().__init__()
        self.setObjectName("Menu")
        self.story = Story()

        font_button = QtGui.QFont()
        font_button.setFamily("Arial")
        font_button.setPointSize(18)
        font_label = QtGui.QFont()
        font_label.setFamily("Arial")
        font_label.setPointSize(24)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(390, 30, 200, 40))
        self.label.setFont(font_label)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("請選擇一段故事")

        self.label_image = QtWidgets.QLabel(self)
        self.label_image.setGeometry(QtCore.QRect(290, 100, 400, 100))
        self.label_image.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_image.setObjectName("label_Image")
        # self.label_image.setScaledContents(True)  # 啟用圖片自動縮放

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(250, 230, 500, 40))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.combo_box_select_changed)

        self.label_intro = QtWidgets.QLabel(self)
        self.label_intro.setGeometry(QtCore.QRect(250, 280, 500, 170))
        self.label_intro.setFont(font_button)
        self.label_intro.setText("")
        self.label_intro.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_intro.setObjectName("label_Intro")
        self.label_intro.setWordWrap(True)

        self.button_back = QtWidgets.QPushButton(self)
        self.button_back.setGeometry(QtCore.QRect(770, 300, 91, 41))
        self.button_back.setFont(font_button)
        self.button_back.setObjectName("Button_Back")
        self.button_back.setText("上一頁")
        self.button_back.clicked.connect(self.show_login)

        self.button_confirm = QtWidgets.QPushButton(self)
        self.button_confirm.setGeometry(QtCore.QRect(770, 400, 91, 41))
        self.button_confirm.setFont(font_button)
        self.button_confirm.setObjectName("Button_Confirm")
        self.button_confirm.setText("選定")
        self.button_confirm.clicked.connect(self.show_main)

        # 新增"結束遊戲"按鈕
        self.button_quit = QtWidgets.QPushButton(self)
        self.button_quit.setGeometry(QtCore.QRect(10, 445, 120, 35))  # 設定按鈕的位置和大小
        self.button_quit.setFont(font_button)
        self.button_quit.setObjectName("Button_Quit")
        self.button_quit.setText("結束遊戲")
        self.button_quit.clicked.connect(self.check_quit)  # 連接到退出遊戲的處理函數

        QtCore.QMetaObject.connectSlotsByName(self)

        self.load_combo_box()


    def load_combo_box(self):
        for num in range(1, self.story.get_len()+1):
            self.comboBox.addItem(f"故事{num}")

    def combo_box_select_changed(self, index):
        self.label_intro.setText(self.story.get_intro(index+1))
        pixmap = QtGui.QPixmap(self.story.get_image(index+1))
        scaled_pixmap = pixmap.scaled(self.label_image.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label_image.setPixmap(scaled_pixmap)

    def show_main(self):
        self.switch_window.emit(self.comboBox.currentIndex()+1)

    def show_login(self):
        self.back_window.emit()

    def check_quit(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("確定要結束遊戲嗎？")
        msgBox.setWindowTitle("退出確認")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            QtWidgets.QApplication.quit()
