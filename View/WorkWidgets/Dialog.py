import sys
from PyQt5 import QtGui, QtWidgets

class Dialog(QtWidgets.QDialog):
    def __init__(self, title, msg):
        super().__init__()
        self.setWindowTitle(title)
        
        font = QtGui.QFont()
        if sys.platform == "win32":
            font.setFamily("Microsoft JhengHei UI")
            font.setPointSize(12)
        else:
            font.setFamily("Arial")
            font.setPointSize(14)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.setCenterButtons(True)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(msg)
        message.setFont(font)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
    
    def accept(self):
        self.close()
