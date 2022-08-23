import os
import sys
import pymysql
import requests
import login,make_party

from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
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
    def __init__(self):
        super(main_class,self).__init__()
        self.initui()
        self.setWindowTitle('MAIN')
    def initui(self):
        self.setupUi(self)


    


#######################################################################################################
        #왼쪽 상단 접속 아이디 표시부분
        self.login_id_name.setText(login.result_login[0][2]+" 님")

#######################################################################################################    
        #내 정보보기 부분
        #데이터베이스 연결
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
        cursor = conn.cursor()

        #sql구문 실행
        sql = "select charname,charlevel,charjob from havechar where userinfo_userid = '%s' ORDER BY charlevel DESC;" % login.input_login_userid
        cursor.execute(sql)
        #sql구문 실행한 결과값을 result에 대입
        result = cursor.fetchall()
        conn.close()

        for i in result:
            char_list = " ".join(i)
            #콤보박스 요소 추가하는 코드
            self.char_cho.addItem(char_list)

    #선택하기 부분 누르면 선택캐릭터 스팩 보이는 함수
    def mychar_info(self):
        #선택한 commbo박스안의 요소를 ' '를 기준으로 슬라이싱 해서 split_char_list로 가져오기
        char_list=self.char_cho.currentText()
        split_char_list=char_list.split(' ')
        
        self.char_cho_name.setText(split_char_list[0])
        self.char_cho_level.setText(split_char_list[1])
        self.char_cho_job.setText(split_char_list[2])



#######################################################################################################


#######################################################################################################
#만들어진 파티 부분
    #파티선택 버튼
    def look_at_party(self):
        pass



#######################################################################################################


#######################################################################################################
#파티자리 확인 부분
    #파티신청버튼
    def join_party(self):
        pass



#######################################################################################################


#######################################################################################################
#내가만든파티 부분
    #파티만들기 버튼
    def make_party_step(self):
        self.make_party_page = make_party.make_party_class()
        self.make_party_page.show()   
        
    #파티취소 버튼
    def drop_party(self):
        pass

#######################################################################################################


#######################################################################################################
#신청한파티 부분
    #신청취소버튼
    def drop_joinparty(self):
        pass



#######################################################################################################



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = login.login_class()
    myWindow.show()
    app.exec_()