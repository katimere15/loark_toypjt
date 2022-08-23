import os
import sys
import pymysql
import signin
import main
from PyQt5.QtWidgets import *
from PyQt5 import uic



def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
#로그인 화면 파일 연결
loginwindow_form = resource_path("./ui/loginwindow.ui")
loginwindow_form_class = uic.loadUiType(loginwindow_form)[0]



#로그인 창
class login_class(QDialog,QWidget,loginwindow_form_class):
    def __init__(self):
        super(login_class,self).__init__()
        self.initui()
        self.setWindowTitle('로그인창')
    def initui(self):
        self.setupUi(self)
    #로그인 버튼 눌렀을 때 이밴트    
    def login_step(self):
        global input_login_userid
        global result_login

        input_login_userid = self.login_userid.text() #login_userid text 값 가져오기
        input_login_userpw = self.login_userpw.text() #login_userpw text 값 가져오기
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
        cursor = conn.cursor()

        sql = "SELECT userid,userpw,top_char FROM userinfo where userid = '%s'" % input_login_userid
        cursor.execute(sql)

        result_login = cursor.fetchall()
        #대표캐릭터 이름 가져오기
        
        conn.close()

        #공백,아이디,비번확인 하는 함수
        def input_info_check(self,result_login,id,pw):
            #아이디나 비번 공백일떄 
            if not id or not pw:
                QMessageBox.information(self,"다시입력","뭐하심?? 나 놀림??? 아디 비번 확실히 입력하셈")
            #모든 정보를 입력받고 데이터베이스에서 회원정보 비교
            elif not result_login:
                QMessageBox.information(self,"닫기","회원가입부터 하시져")
            elif pw != result_login[0][1]:
                QMessageBox.information(self,"다시입력","뭐해 비번틀렸잖아 바뻐!")
            else:
                QMessageBox.information(self,"시작하기","이랏샤이마세")

                # 로그인페이지 닫기
                self.close()
                #메인페이지 오픈
                self.main = main.main_class()    
                self.main.show()

        input_info_check(self,result_login,input_login_userid,input_login_userpw)
        




    #회원가입 버튼눌렀을떄 이밴트
    def signin_step(self):
        self.close()                     # 로그인페이지 닫기
        # 회원가입 페이지 오픈
        self.signin_page = signin.signin_class()
        self.signin_page.show()                     