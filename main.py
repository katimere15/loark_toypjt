import os
import sys
import pymysql
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
#회원가입 화면 파일 연결
signinwindow_form = resource_path("./ui/signinwindow.ui")
signinwindow_form_class = uic.loadUiType(signinwindow_form)[0]
#메인 화면 파일 연결
main_form = resource_path("./ui/main.ui")
main_form_class = uic.loadUiType(main_form)[0]

#로그인 창
class login_Class(QDialog,QWidget,loginwindow_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('로그인창')
        self.show()

    #로그인 버튼 눌렀을 때 이밴트    
    def login_step(self):
        input_login_userid = self.login_userid.text() #login_userid text 값 가져오기
        input_login_userpw = self.login_userpw.text() #login_userpw text 값 가져오기
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
        cursor = conn.cursor()

        sql = "SELECT * FROM userinfo where userid = '%s'" % input_login_userid
        cursor.execute(sql)

        result = cursor.fetchall()
        conn.close()

        #공백,아이디,비번확인
        if not result:
            QMessageBox.information(self,"다시입력","공백이거나 아이디를 찾을 수 없습니다. 아이디를 확인하시거나 회원가입을 진행해주세요")
        elif result:
            if input_login_userpw != result[0][1]:
                QMessageBox.information(self,"다시입력","비밀번호가 틀렸습니다.(잊어버린거 아니죠??? 그렇죠??)")
            else:
                QMessageBox.information(self,"시작하기","어섭셔~~~ 회원님 입장하신다~~")
                self.close()                     #로그인 페이지 종료
                self.second = main_class()    #메인페이지 오픈

    #회원가입 버튼눌렀을떄 이밴트
    def signin_step(self):
        self.hide()                     # 로그인페이지 숨김
        self.second = signin_class()    # 회원가입 페이지 오픈
        self.second.exec()              # 회원가입 대기
        self.show()                     # 로그인 페이지 보이기


#메인 창
class main_class(QMainWindow,main_form_class):
    def __init__(self):
        super(main_class,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)
        self.setWindowTitle('메인')
        

    













#회원가입 창
class signin_class(QDialog,QWidget,signinwindow_form_class):
    def __init__(self):
        super(signin_class,self).__init__()
        self.initUi()
        self.show()
    def initUi(self):
        self.setupUi(self)
        self.setWindowTitle('회원가입창')

    #회원가입 창에서 만들기 버튼 누를때 이밴트
    def userinfo_push(self):
        input_signin_userid = self.signin_userid.text() #signin_userid text 값 가져오기
        input_signin_userpw = self.signin_userpw.text() #signin_userpw text 값 가져오기
        input_signin_topchar = self.signin_topchar.text() #signin_topchar text 값 가져오기
        if not input_signin_userid:
            QMessageBox.information(self,"공백없이 ok?","뭐해에에에엑!!!! 아이디 공백이잖아!!!!!!")
        elif not input_signin_userpw:
           QMessageBox.information(self,"공백없이 ok?","뭐해에에에엑!!!! 비밀번호 공백이잖아!!!!!!")
        elif not input_signin_topchar:
           QMessageBox.information(self,"공백없이 ok?","뭐해에에에엑!!!! 대표캐릭터이름 공백이잖아!!!!!!")
        else:
            conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
            cursor = conn.cursor()

            sql_check = "SELECT * FROM userinfo where userid = '%s'" % input_signin_userid
            cursor.execute(sql_check)
            result = cursor.fetchall()

            if not result:
                sql = "INSERT INTO userinfo (userid,userpw,top_char,step) VALUES (%s, %s, %s ,%s)"
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(sql, (input_signin_userid, input_signin_userpw, input_signin_topchar, 1))
                        conn.commit()
                QMessageBox.information(self,"로그인창으로","회원가입이 완료되었습니다.(비밀번호 까먹지말아줘 찾는거 수작업이야...)")
                self.close() #클릭시 종료
            
            else:
                QMessageBox.information(self,"다시입력하기","사용중인 아이디입니다. 다시입력하십셔")

    #회원가입 창에서 돌아가기 버튼 누를때 이밴트
    def return_login(self):
        self.close()




    


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = login_Class() 
    window.show()
    app.exec_()