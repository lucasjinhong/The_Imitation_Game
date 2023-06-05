if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from PyQt5 import QtCore, QtGui, QtWidgets
from Function.Story import Story

class Menu(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(int) # 換到Main_Widget要用的
    back_window = QtCore.pyqtSignal() # 回到Login要用的

    def __init__(self):
        super().__init__()
        self.setObjectName("ui_2")
        self.story = Story()

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font1 = QtGui.QFont()
        font1.setFamily("Arial")
        font1.setPointSize(16)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(390, 60, 210, 40))
        self.label.setFont(font1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("請選擇一段故事")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(360, 110, 271, 81))
        self.label_2.setObjectName("label_Image")
        self.label_2.setScaledContents(True)  # 啟用圖片自動縮放
        pixmap = QtGui.QPixmap("./Resource/door.jpeg")
        scaled_pixmap = pixmap.scaled(self.label_2.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label_2.setPixmap(scaled_pixmap)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(260, 230, 451, 170))
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_Intro")
        self.label_3.setWordWrap(True)

        self.button_back = QtWidgets.QPushButton(self)
        self.button_back.setGeometry(QtCore.QRect(770, 300, 91, 41))
        self.button_back.setFont(font)
        self.button_back.setObjectName("Button_Back")
        self.button_back.setText("上一頁")
        self.button_back.clicked.connect(self.show_login)

        self.button_confirm = QtWidgets.QPushButton(self)
        self.button_confirm.setGeometry(QtCore.QRect(770, 400, 91, 41))
        self.button_confirm.setFont(font)
        self.button_confirm.setObjectName("Button_Confirm")
        self.button_confirm.setText("選定")
        self.button_confirm.clicked.connect(self.show_main)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(250, 400, 451, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentIndexChanged.connect(self.combo_box_select_changed)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.load_combo_box()

    def load_combo_box(self):
        for num in range(1, self.story.get_len()+1):
            self.comboBox.addItem(f"故事{num}")

    def combo_box_select_changed(self, index):
        self.label_3.setText(self.story.get_intro(index+1))

    def show_main(self):
        self.switch_window.emit(self.comboBox.currentIndex()+1)

    def show_login(self):
        self.back_window.emit()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Menu()
    main_window.setFixedSize(1000, 500)
    main_window.show()
    sys.exit(app.exec_())
