import sys
from PyQt5 import QtWidgets
from View.WorkWidgets.Login import Login
from View.WorkWidgets.Menu import Menu
from View.WorkWidgets.Main_Widget import Main_Widget

class Controller:
    def __init__(self, scaleRate):
        self.username = ""
        self.scaleRate = scaleRate
    
    def show_login(self):
        self.login = Login(self.scaleRate)
        self.login.switch_window.connect(self.show_menu)
        self.window_show(self.login)
    
    def show_menu(self, text):
        self.username = text
        self.menu = Menu()
        self.menu.switch_window.connect(self.show_main)
        self.menu.back_window.connect(self.show_login_from_menu)
        self.login.close()
        #window_show(self.menu)
        self.menu.setFixedSize(1000, 500)
        self.menu.setWindowTitle("The Imitation Game")
        self.menu.show()
    
    def show_main(self, index):
        self.main = Main_Widget(self.username, index)
        self.main.back_window.connect(self.show_menu_from_main)
        self.menu.close()
        #window_show(self.main)
        self.main.setFixedSize(1000, 500)
        self.main.setWindowTitle("The Imitation Game")
        self.main.show()
    
    def show_login_from_menu(self): 
        self.menu.close()
        #self.window_show(self.login)
        self.show_login()
    
    def show_menu_from_main(self):
        self.main.close()
        #self.window_show(self.menu)
        self.show_menu(self.username)
    
    def window_show(self, win, width=1000, height=500):
        win.setFixedSize(int(width * self.scaleRate), int(height * self.scaleRate))
        win.setWindowTitle("The Imitation Game")
        win.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    scaleRate = app.screens()[0].logicalDotsPerInch()/96
    controller = Controller(scaleRate)
    controller.show_login()
    sys.exit(app.exec_())
