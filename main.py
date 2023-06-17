import sys
from PyQt5 import QtWidgets, sip
from View.WorkWidgets.Login import Login
from View.WorkWidgets.Menu import Menu
from View.WorkWidgets.Main_Widget import Main_Widget

class Controller:
    def __init__(self):
        self.username = ""

    def show_login(self):
        self.login = Login()
        self.login.setFixedSize(1000, 500)
        self.login.setWindowTitle("The Imitation Game")
        self.login.switch_window.connect(self.show_menu)
        self.login.show()

    def show_menu(self, text):
        self.username = text
        self.menu = Menu()
        self.menu.setFixedSize(1000, 500)
        self.menu.setWindowTitle("The Imitation Game")
        self.menu.switch_window.connect(self.show_main)
        self.menu.back_window.connect(self.show_login_from_menu)
        self.login.close()
        self.menu.show()

    def show_main(self, index):
        self.main = Main_Widget(self.username, index)
        self.main.setFixedSize(1000, 500)
        self.main.setWindowTitle("The Imitation Game")
        self.main.back_window.connect(self.show_menu_from_main)
        self.menu.close()
        self.main.show()

    def show_login_from_menu(self): # 從menu回到login
        self.menu.close()
        self.show_login()

    def show_menu_from_main(self): # 從main回到menu
        self.main.close()
        self.show_menu(self.username)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())
