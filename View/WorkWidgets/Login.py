from PyQt5 import QtCore, QtGui, QtWidgets
from View.WorkWidgets.Dialog import Dialog

class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setObjectName("login")
        self.setup_ui()

    def setup_ui(self):
        font_label = self.create_font("Arial", 20)
        font_button = self.create_font("Arial", 20)
        font_title = self.create_font("Arial", 108)

        self.label_image = self.create_label(0, 0, 1000, 500, "label_Image", None, image_path="./View/Resource/login/login")
        self.title = self.create_label(170, 20, 700, 200, "title", "模 仿 遊 戲", font_title)
        self.label = self.create_label(235, 400, 210, 40, "label", "使用者名稱", font_label)
        self.textEdit = self.create_text_edit(390, 400, 200, 35, "textEdit", font_label)

        self.title.setStyleSheet("color: white;")
        self.label.setStyleSheet("color: white;")

        self.button_confirm = QtWidgets.QPushButton(self)
        self.button_confirm.setGeometry(QtCore.QRect(640, 400, 100, 35))
        self.button_confirm.setFont(font_button)
        self.button_confirm.setObjectName("button_confirm")
        self.button_confirm.setText("確定")
        self.button_confirm.clicked.connect(self.button_click)

    def create_font(self, family, size):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
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
        textEdit = QtWidgets.QTextEdit(self)
        textEdit.setGeometry(QtCore.QRect(x, y, width, height))
        textEdit.setFont(font)
        textEdit.setObjectName(obj_name)
        return textEdit

    def button_click(self):
        if len(self.textEdit.toPlainText()) > 0:
            self.show_menu()
        else:
            dlg = Dialog("Error", "User name 不可為空")
            dlg.exec()

    def show_menu(self):
        self.switch_window.emit(self.textEdit.toPlainText())
