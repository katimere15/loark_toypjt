import os
import sys
import pymysql
import signin
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import uic


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# #메인 화면 파일 연결
form = resource_path("./ui/login.ui")
form_class = uic.loadUiType(form)[0]



###########################################################################################################################################################

# #데이터베이스 연결해서 유저정보 가져오기 베이스
# sql = ""
# conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')

# with conn:
#     with conn.cursor() as cur:
#         cur.execute(sql, ())
#         conn.commit()

###########################################################################################################################################################




















class login_class(QMainWindow, form_class):

    #클래스가 작동하면 db연결해서 유저정보 데이터를 가져온다
    userdata_sql = "select * from user_table"
    #클래스가 작동하면 db연결해서 등록된 캐릭터 데이터를 가져온다.
    usercharter_sql = "select * from charter_table"
    conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='party', charset='utf8')
    curs = conn.cursor()
    #유저정보 저장
    curs.execute(userdata_sql)
    userdata = curs.fetchall()
    #캐릭터정보 저장
    curs.execute(usercharter_sql)
    usercharter = curs.fetchall()
    curs.close()
    conn.close()
    


    #db에서 가져온 데이터 pandas로 정리
    userdata_df = pd.DataFrame(userdata,columns=['아이디','비밀번호','대표캐릭터'])
    usercharter_df = pd.DataFrame(usercharter,columns=['유저아이디','캐릭터이름','캐릭터래벨','캐릭터직업'])


    def __init__(self):
        super(login_class,self).__init__()
        self.initui()
        self.setWindowTitle('login')
    def initui(self):
        self.setupUi(self)

    #로그인 버튼 눌렀을떄 이벤트
    def login_step(self):
        pass
    
    #회원가입 버튼눌렀을떄 이벤트
    def signin_step(self):
        self.close()                     # 로그인페이지 닫기
        # 회원가입 페이지 오픈
        self.signin_page = signin.signin_class()
        self.signin_page.show()   

