import os
import sys
import pymysql
import requests

from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# #메인 화면 파일 연결
main_form = resource_path("./ui/main.ui")
main_form_class = uic.loadUiType(main_form)[0]



#메인 창
class main_class(QMainWindow, main_form_class):
    #로그인 id데이터 가져오기
    login_txt = open("./txt/login_info.txt", 'r')
    #로그인 id데이터를 변수에 저장
    login_userid = login_txt.readline()
    login_txt.close()






    def __init__(self):
        super().__init__()
        self.setupUi(self)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = main_class()
    myWindow.show()
    app.exec_()