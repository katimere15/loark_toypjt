import os
import sys
import pandas as pd
import requests
import pymysql
import login
import def_index
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#회원가입 화면 파일 연결
signinwindow_form = resource_path("./ui/signin.ui")
signinwindow_form_class = uic.loadUiType(signinwindow_form)[0]

#db연결
conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='party', charset='utf8')


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
    def make_userinfo_step(self):
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
            #가져온 유저 테이블 데이터
            curs = conn.cursor()
            usercharter_sql = "select * from charter_table"
            curs.execute(usercharter_sql)
            usercharter = curs.fetchall()

            usercharter_df = pd.DataFrame(usercharter,columns=['유저아이디','캐릭터이름','캐릭터래벨','캐릭터직업'])

        #login.login_class.userdata_df['아이디']안에 입력한 아이디값이 있을경우 
            if (login.login_class.userdata_df['아이디']==input_signin_userid).any():
                QMessageBox.information(self,"다시입력하기","사용중인 아이디임. 다시입력하셈")

                #login_page.login_class.usercharter_df['캐릭터이름']안에 입력한 대표캐릭 값이 있는경우
            elif(usercharter_df['캐릭터이름']==input_signin_topchar).any():
                QMessageBox.information(self,"다시입력하기","이 캐릭터는 이미 회원가입된 상태인거 같은대 이 오류가 계속나오면 SevenNight/어머 로 DM보내셈")

            else:
                #대표캐릭터이름으로 보유하고있는 모든 캐릭터정보를 스크래핑해옴
                mycharters = def_index.return_all_havechar("https://lostark.game.onstove.com/Profile/Character/%s"%input_signin_topchar)

                #대표캐릭터가 검색되지않을 경우 
                len_mycharters=len(mycharters)
                if len_mycharters == 0:
                    QMessageBox.information(self,"다시입력하기","뭐임 대표캐릭터이름 다시확인점")
                #정상적으로 데이터를 불러왔을때 userid테이블에 정보입력
                elif len_mycharters != 0:
                    
                    
                    user_sql = "INSERT INTO `party`.`user_table` (`userid`, `userpw`, `maincharter`) VALUES ('%s', '%s', '%s')"%(input_signin_userid, input_signin_userpw, input_signin_topchar)
                    curs.execute(user_sql)
                    conn.commit()

                    #정상적으로 데이터를 불러왔을때 charter테이블에 정보입력
                    for i in mycharters:
                        mycharters_info = def_index.return_charinfo("https://lostark.game.onstove.com/Profile/Character/%s"%i)

                        #db에 입력한 값 보내기
                        mycharters_info_sql = "INSERT INTO `party`.`charter_table` (`userid`, `charter_name`, `charter_level`, `charter_class`) VALUES ('%s','%s','%s','%s');"%(input_signin_userid,mycharters_info[0],mycharters_info[1],mycharters_info[2])
                        curs = conn.cursor()
                        curs.execute(mycharters_info_sql)
                        conn.commit()

                    QMessageBox.information(self,"ok","회원가입 완료되었셈")
                    #회원가입 페이지 닫기
                    self.close()
                    #로그인 페이지 열기
                    self.login_page = login.login_class()
                    self.login_page.show() 





    #회원가입 창에서 돌아가기 버튼 누를때 이밴트
    def return_login(self):
        #회원가입 페이지 닫기
        self.close()
        #로그인 페이지 열기
        self.login_page = login.login_class()
        self.login_page.show()   