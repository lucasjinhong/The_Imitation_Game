import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from View.WorkWidgets.Dialog import Dialog

class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, scaleRate):
        super().__init__()
        self.setObjectName("login")
        self.scaleRate = scaleRate
        self.setup_ui()

    def setup_ui(self):
        self.font_button = QtGui.QFont()
        self.font_button = QtGui.QFont()
        
        if sys.platform == "win32":
            # Win
            font_label = self.create_font("Microsoft JhengHei UI", 20, bold=True)
            font_button = self.create_font("Microsoft JhengHei UI", 20)
            font_title = self.create_font("Microsoft JhengHei UI", 88)
        else:
            # Mac
            font_label = self.create_font("Arial", 20)
            font_button = self.create_font("Arial", 20)
            font_title = self.create_font("Arial", 108)
        

        self.label_image = self.create_label(int(0*self.scaleRate), int(0*self.scaleRate), int(1000*self.scaleRate), int(500*self.scaleRate), "label_Image", None, image_path="./View/Resource/login/login")
        self.title = self.create_label(int(170*self.scaleRate), int(20*self.scaleRate), int(700*self.scaleRate), int(200*self.scaleRate), "title", "模 仿 遊 戲", font_title)
        self.label = self.create_label(int(235*self.scaleRate), int(400*self.scaleRate), int(210*self.scaleRate), int(40*self.scaleRate), "label", "使用者名稱", font_label)
        self.textEdit = self.create_text_edit(int(390*self.scaleRate), int(400*self.scaleRate), int(200*self.scaleRate), int(35*self.scaleRate), "textEdit", font_label)

        self.title.setStyleSheet("color: white;")
        self.label.setStyleSheet("color: white;")

        self.button_confirm = QtWidgets.QPushButton(self)
        self.button_confirm.setGeometry(QtCore.QRect(int(640*self.scaleRate), int(400*self.scaleRate), int(100*self.scaleRate), int(35*self.scaleRate)))
        self.button_confirm.setFont(font_button)
        self.button_confirm.setObjectName("button_confirm")
        self.button_confirm.setText("確定")
        self.button_confirm.clicked.connect(self.button_click)

    def create_font(self, family, size, bold=False):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        if bold == True:
            font.setBold(True)
        return font

    def create_label(self, x, y, width, height, obj_name, text, font=None, image_path=None):
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(x, y, width, height))
        label.setObjectName(obj_name)
        if text:
            formatted_text = f"<pre>{text}</pre>"
            label.setText(formatted_text)
        if font:
            label.setFont(font)
        if image_path:
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setScaledContents(True)
            pixmap = QtGui.QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(scaled_pixmap)
        return label

    def create_text_edit(self, x, y, width, height, obj_name, font):
        textEdit = QtWidgets.QLineEdit(self)
        textEdit.setGeometry(QtCore.QRect(x, y, width, height))
        textEdit.setFont(font)
        textEdit.setObjectName(obj_name)
        return textEdit

    def button_click(self):
        if len(self.textEdit.text()) > 0:
            self.show_menu()
        else:
            dlg = Dialog("Error", "User name 不可為空")
            dlg.exec()

    def show_menu(self):
        self.switch_window.emit(self.textEdit.text())
