import os
import sys
import login

from PyQt5.QtWidgets import *
from PyQt5 import uic


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# #메인 화면 파일 연결
main_form = resource_path("./ui/main.ui")
main_form_class = uic.loadUiType(main_form)[0]


class main_class(QDialog,QWidget, main_form_class):
    def __init__(self):
        super(main_class,self).__init__()
        self.initui()
        self.setWindowTitle('login')
    def initui(self):
        self.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = login.login_class()
    myWindow.show()
    app.exec_()