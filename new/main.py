import os
import sys
import login
import pymysql
import make_party
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
        global login_myid
        global usercharter
        global usertopcharter
        self.setupUi(self)

        #로그인창에서 로그인 성공했을떄 id정보를 가져옴
        login_myid=login.input_login_userid
        #가져온 로그인 id로 보유캐릭터 테이블에서 데이터 가져옴
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='party', charset='utf8')
        curs = conn.cursor()
        usercharter_sql = "select * from charter_table where userid ='%s'"%login_myid
        curs.execute(usercharter_sql)
        usercharter = curs.fetchall()

        usertopcharter = login.mytopcharter
        

        


    

    def partymake_btn(self):
        
        self.main_class = make_party.make_party_class()
        self.main_class.exec()
        #파티보이는 창 리셋
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = login.login_class()
    myWindow.show()
    app.exec_()