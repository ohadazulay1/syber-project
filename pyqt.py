from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class FirstWindow(QMainWindow):

    def __init__(self):
        super(FirstWindow, self).__init__()
        self.initUI()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("First window")


    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Welcome")
        self.label.move(50, 50)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Sign up")
        self.button1.move(50, 80)
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        print("Clicked")
        #comment 123

def firstWindow():
    app = QApplication(sys.argv)
    win = FirstWindow()
    win.show()
    sys.exit(app.exec_())

firstWindow()