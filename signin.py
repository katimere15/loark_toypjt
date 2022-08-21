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

#회원가입 화면 파일 연결
signinwindow_form = resource_path("./ui/signinwindow.ui")
signinwindow_form_class = uic.loadUiType(signinwindow_form)[0]




#회원가입 창
class signin_class(QDialog,QWidget,signinwindow_form_class):
    
    ############################################
    #대표 캐릭터이름으로 보유하고있는 모든 캐릭터(all_have_char) 데이터를 가져오는 함수 
    def return_all_havechar(address):
        res = requests.get(address)
        soup = BeautifulSoup(res.text, 'html.parser')
        charname_low = soup.select('#expand-character-list > ul > li > span > button > span')
        all_have_char=[]
        #캐릭터명 
        for i in charname_low:
            all_have_char.append(i.text)
        return all_have_char

    ############################################
    #캐릭터 이름과,레벨,직업 정보를 가져와 변수에 저장하는 함수
    def return_charlevel(address):
        res = requests.get(address)
        soup = BeautifulSoup(res.text, 'html.parser')
        char_name = soup.select_one("#lostark-wrapper > div > main > div > div.profile-character-info > span.profile-character-info__name").text
        char_level = soup.select_one('#lostark-wrapper > div > main > div > div.profile-ingame > div.profile-info > div.level-info2 > div.level-info2__expedition > span:nth-child(2)').text
        char_job = soup.select_one("#lostark-wrapper > div > main > div > div.profile-character-info > img")["alt"]
        return char_name,char_level,char_job

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

            #아이디 체크
            sql_check = "SELECT userid FROM userinfo where userid = '%s'" % input_signin_userid
            cursor.execute(sql_check)
            result = cursor.fetchall()
            #데이터베이스 캐릭터 체크
            sql_char_check = "SELECT charname FROM havechar where charname = '%s'" % input_signin_topchar
            cursor.execute(sql_char_check)
            result2 = cursor.fetchall()


            if result:
                QMessageBox.information(self,"다시입력하기","사용중인 아이디입니다. 다시입력하십셔")
            elif result2:
                QMessageBox.information(self,"다시입력하기","사용중인 캐릭터이름입니다. 다시입력하십셔")

            
            else:
                #대표 캐릭터이름으로 보유하고있는 모든 캐릭터(all_have_char) 데이터를 가져오는 함수
                all_have_charname=signin_class.return_all_havechar("https://lostark.game.onstove.com/Profile/Character/%s" %input_signin_topchar)
                all_have_char_count=len(all_have_charname)
                #대표캐릭터이름으로 검색실패시 메시지 출력 성공시 정보 가져옴
                if all_have_charname == 0:
                    QMessageBox.information(self,"다시입력하기","뭐임 대표캐릭터이름 다시확인점")
                else:
                    #userid테이블에 정보입력
                    sql = "INSERT INTO userinfo (userid,userpw,top_char,step) VALUES (%s, %s, %s ,%s)"
                    with conn:
                        with conn.cursor() as cur:
                            cur.execute(sql, (input_signin_userid, input_signin_userpw, input_signin_topchar, 1))
                            conn.commit()
                        
                        #튜플로 가져온 all_have_charname 만큼 그 캐릭터의 이름,레벨,직업 정보를 가져온다.
                        for j in range(all_have_char_count):
                            char_info=[]
                            char_info.extend(signin_class.return_charlevel("https://lostark.game.onstove.com/Profile/Character/%s" %all_have_charname[j]))

                            #위에서 입력받은 대표캐릭터 이름으로 havechar테이블에 보유캐릭터 정보 입력
                            sql2 = "INSERT INTO havechar (userinfo_userid,charname,charlevel,charjob) VALUES (%s, %s, %s ,%s)"
                            conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
                            cursor = conn.cursor()

                            with conn:
                                with conn.cursor() as cur:
                                    cur.execute(sql2, (input_signin_userid,char_info[0],char_info[1],char_info[2]))
                                    conn.commit()
                            char_info=[]



                QMessageBox.information(self,"로그인창으로","회원가입이 완료되었습니다.(비밀번호 까먹지말아줘 찾는거 수작업이야...)")
                self.close() #클릭시 종료
            

    #회원가입 창에서 돌아가기 버튼 누를때 이밴트
    def return_login(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = signin_class()
    myWindow.show()
    app.exec_()