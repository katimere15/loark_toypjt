import os
import sys


from PyQt5.QtWidgets import *
from PyQt5 import uic


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# #메인 화면 파일 연결
form = resource_path(".ui경로.ui")
form_class = uic.loadUiType(form)[0]


class class_name(QDialog,QWidget, form_class):
    def __init__(self):
        super(class_name,self).__init__()
        self.initui()
    def initui(self):
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = class_name()
    myWindow.show()
    app.exec_()