if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from PyQt5 import QtCore, QtGui, QtWidgets
from WorkWidgets.Dialog import Dialog

class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setObjectName("ui_1")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font1 = QtGui.QFont()
        font1.setFamily("Arial")
        font1.setPointSize(16)

        self.label_image = QtWidgets.QLabel(self)
        self.label_image.setGeometry(QtCore.QRect(0, 0, 1000, 500)) # 如果換圖片，要改這邊
        self.label_image.setObjectName("label_Image")
        self.label_image.setScaledContents(True)
        pixmap = QtGui.QPixmap("./Resource/Designer.png") # 設定要放什麼圖片
        scaled_pixmap = pixmap.scaled(self.label_image.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label_image.setPixmap(scaled_pixmap)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(170, 400, 210, 40))
        self.label.setFont(font1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("使用者名稱")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(390, 400, 200, 35))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(QtCore.QRect(640, 400, 100, 35))
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.button.setText("確定")
        self.button.clicked.connect(self.button_click)

        QtCore.QMetaObject.connectSlotsByName(self)

    def button_click(self):
        if len(self.textEdit.toPlainText()) > 0:
            self.show_menu()
        else:
            dlg = Dialog("Error", "User name 不可為空")
            dlg.exec()

    def show_menu(self):
        self.switch_window.emit(self.textEdit.toPlainText())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Login()
    main_window.setFixedSize(1000, 500)
    main_window.show()
    sys.exit(app.exec_())
