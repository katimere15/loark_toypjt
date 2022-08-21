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

        #공백,아이디,비번확인 하는 함수
        def input_info_check(self,result,id,pw):
            #아이디 비번 둘다 공백일떄
            if not id and pw:
                QMessageBox.information(self,"다시입력","뭐하심?? 나 놀림??? 아디 비번 입력하셈")
            #아이디만 공백이거나 데이터베이스에서 아이디를 찾을수 없을때
            elif not id:
                QMessageBox.information(self,"다시입력","공백이거나 아이디를 찾을 수 없으셈. 아이디를 확인하시거나 회원가입을 진행해주셈")
            #비밀번호가 공백일떄
            elif not pw:
                QMessageBox.information(self,"다시입력","비번이 공백이잖슴 비밀번호 입력하셈")            
            #모든 정보를 입력받고 데이터베이스에서 회원정보 비교
            elif result:
                #비밀번호 틀림 
                if pw != result[0][1]:
                    QMessageBox.information(self,"다시입력","비밀번호가 틀렸심.(잊어버린거 아니죠??? 그렇죠??)")
                #로그인 성공
                else:
                    QMessageBox.information(self,"시작하기","어섭셔~~~ 회원님 입장하신다~~")
                    #txt폴더의 login_info파일에 로그인 성공한 정보 입력
                    f = open("./txt/login_info.txt", 'w')
                    info_data = input_login_userid
                    f.write(info_data)
                    f.close()

                    # 로그인페이지 숨김
                    self.hide()
                    #메인페이지 오픈
                    self.mainpage = main.main_class()    
                    self.mainpage.show()

        input_info_check(self,result,input_login_userid,input_login_userpw)





    #회원가입 버튼눌렀을떄 이밴트
    def signin_step(self):
        self.hide()                     # 로그인페이지 숨김
        self.signin_page = signin.signin_class()    # 회원가입 페이지 오픈
        self.signin_page.exec()              # 회원가입 대기
        self.show()                     # 로그인 페이지 보이기

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = login_Class() 
    window.show()
    app.exec_()