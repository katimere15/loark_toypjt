import os
import sys
import pymysql
import requests
import login,make_party
from datetime import datetime
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
        #데이터베이스에서 가져온 보유캐릭터 정보 넣을 전역변수 선언 
        global have_char_info
        global all_view_party_sql
        global login_my_id
        global login_my_topchar

        login_my_id = login.input_login_userid
        login_my_topchar = login.result_login[0][2]


    


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
        
        #데이터베이스에서 가져온 보유캐릭터 정보 전역변수로 입력
        # 보유캐릭터 정보 넣을 전역변수에 데이터 대입
        have_char_info = result

        for i in have_char_info:
            char_list = " ".join(i)
            #콤보박스 요소 추가하는 코드
            self.char_cho.addItem(char_list)


        # 모든 파티 정보 가져오기
        view_party_sql = "select party_num,party_name,raid_name,party_startdate,party_starttime from party_table where party_startdate > (now()-INTERVAL 1 DAY) order by party_startdate, party_starttime"
        cursor.execute(view_party_sql)
        all_view_party_sql = cursor.fetchall()
        #내 파티 정보 가져오기
        view_my_party_sql="select party_num,party_name,raid_name,party_startdate,party_starttime from party_table where havechar_userinfo_userid = %s"%login.input_login_userid
        cursor.execute(view_my_party_sql)
        my_party_sql = cursor.fetchall()

        #모든 파티정보 입력
        for i in all_view_party_sql:
            str_party= i[1]+"                                               "+str(i[0])+"\n"+i[2] +"\n"+i[3].isoformat()+"\n"+str(i[4])
            self.view_party_info.addItem(str_party)
            # print(str_party)
        #내가 만든 파티정보 입력
        for i in my_party_sql:
            str_myparty= i[1]+"                                               "+str(i[0])+"\n"+i[2] +"\n"+i[3].isoformat()+"\n"+str(i[4])
            self.made_myparty_list.addItem(str_myparty)
            # print(str_party)




    #선택하기 부분 누르면 선택캐릭터 스팩 보이는 함수
    def mychar_info(self):
        #선택한 commbo박스안의 요소를 ' '를 기준으로 슬라이싱 해서 split_char_list로 가져오기
        char_list=self.char_cho.currentText()
        split_char_list=char_list.split(' ')
        
        self.char_cho_name.setText(split_char_list[0])
        self.char_cho_level.setText("LV.  "+split_char_list[1])
        self.char_cho_job.setText(split_char_list[2])



#######################################################################################################


#######################################################################################################

    #만들어진파티 부분에서 리스트를 클릭하면 그 파티에 신청한 맴버 보기
    def view_partymember(self):
        self.view_partyseat_info.clear()
        select_partylist_item = self.view_party_info.selectedItems()
        for i in select_partylist_item:
            #파티 리스트에 숨겨둔 party_num값 구해오기
            text_output= i.text()
            text_output2=text_output.splitlines()
            text_output3=text_output2[0].split("                                               ")
            
            
            global select_party_num
            select_party_num = text_output3[1]
            #party_num 값은 text_output3[1] 이다.
            #party_name값은 text_output3[0] 이다.
        #선택한 파티 이름 보여주기
        self.cho_party_title.setText(text_output3[0])

        #파티맴버 리스트 가져와 추가하기
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
        cursor = conn.cursor()
        #위에서 구한 party_num값과 같은 데이터를 member테이블에서 가져온다.
        view_partymember_sql = "select party_member_charname,party_member_charlevel,party_member_charjob from party_member_table where party_table_party_num = %s;"%text_output3[1]
        cursor.execute(view_partymember_sql)
        view_partymember_sql = cursor.fetchall()


        print(text_output2[1])


        #파티멤버테이블에 item추가
        for i in view_partymember_sql:
            str_partymember= i[0]+"\n"+"Lv. "+ i[1] +"\n"+ i[2]
            self.view_partyseat_info.addItem(str_partymember)








        #선택한 파티의 레벨에 따라 내가 신청할 수있는 캐릭터 찾아 radio박스에 넣기

        # 내 모든 캐릭터 정보가 담긴 변수
        # print(have_char_info)

        self.partyjoin_charcho.clear()
        # 선택한 파티의 레이드 종류는 text_output2[1]
        for i in have_char_info:

            if text_output2[1] in ["도비스","도가토"] and int(i[1])>=415:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)

            elif text_output2[1] == "리허설" and int(i[1])>=1385:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)

            elif text_output2[1] == "발탄노말" and int(i[1])>=1415:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)

            elif text_output2[1] in ["비아키스노말","데자뷰"] and int(i[1])>=1430:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)

            elif text_output2[1] in ["발탄하드","발탄헬"] and int(i[1])>=1445:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)


            elif text_output2[1] in ["비아키스하드","비아키스헬"] and int(i[1])>=1460:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)

            elif text_output2[1] in ["쿠크세이튼노말","쿠크세이튼헬"] and int(i[1])>=1475:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)

            elif text_output2[1] == "아브렐슈드노말 1~2" and int(i[1])>=1490:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)

            elif text_output2[1] in ["아브렐슈드노말 1~4","에피데믹"] and int(i[1])>=1500:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)

            elif text_output2[1] == "아브렐슈드노말 5~6" and int(i[1])>=1520:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)
            elif text_output2[1] == "아브렐슈드하드 1~2" and int(i[1])>=1540:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)
            elif text_output2[1] == "아브렐슈드하드 1~4" and int(i[1])>=1550:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)
            elif text_output2[1] == "아브렐슈드하드 5~6" and int(i[1])>=1560:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)
            elif text_output2[1] == "일리아칸노말" and int(i[1])>=1580:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)
            elif text_output2[1] == "일리아칸하드" and int(i[1])>=1600:
                str_partyjoinchar= i[0]+"  Lv. "+ i[1] +"  "+ i[2]
                self.partyjoin_charcho.addItem(str_partyjoinchar)










#######################################################################################################

    #내 파티 부분에서 리스트를 클릭하면 그 파티에 신청한 맴버 보기
    def view_mypartymember(self):
        self.partyjoin_charcho.clear()
        self.view_partyseat_info.clear()
        select_partylist_item = self.made_myparty_list.selectedItems()
        for i in select_partylist_item:
            #파티 리스트에 숨겨둔 party_num값 구해오기
            text_output= i.text()
            text_output2=text_output.splitlines()
            text_output3=text_output2[0].split("                                               ")


            #party_num 값은 text_output3[1] 이다.
            #party_name값은 text_output3[0] 이다.
        #선택한 파티 이름 보여주기
        self.cho_party_title.setText(text_output3[0])

        #파티맴버 리스트 가져와 추가하기
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
        cursor = conn.cursor()
        #위에서 구한 party_num값과 같은 데이터를 member테이블에서 가져온다.
        view_partymember_sql = "select party_member_charname,party_member_charlevel,party_member_charjob from party_member_table where party_table_party_num = %s;"%text_output3[1]
        cursor.execute(view_partymember_sql)
        view_partymember_sql = cursor.fetchall()

        for i in view_partymember_sql:
            str_partymember= i[0]+"\n"+"Lv. "+ i[1] +"\n"+ i[2]
            self.view_partyseat_info.addItem(str_partymember)




#######################################################################################################
#파티자리 확인 부분
    #파티신청버튼
    def join_party(self):
        pass

        # try:
        #     #선택한 radio박스의 데이터를 가져옴
        #     select_charte = self.partyjoin_charcho.currentText()

        #     #데이터베이스에 넣을수 있게 list로 변환
        #     cut_select_charte=select_charte.split("  ")
        #     cut_select_charte[1]=cut_select_charte[1].lstrip("Lv. ")


        #     #radio박스의 데이터를 db에 넣는 sql문
        #     cut_select_charte_sql = "INSERT INTO `lostark`.`party_member_table` (`party_table_party_num`, `party_member_charname`, `party_member_charlevel`, `party_member_charjob`,`userinfo_userid`) VALUES (%s,%s,%s,%s,%s);"
        #     #db의 파티멤버를 조회하는 sql문
        #     partymember_sql = "select party_member_charname,party_member_charlevel,party_member_charjob,userinfo_userid from party_member_table where party_table_party_num = %s;"%select_party_num
        #     #db연결
        #     conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
        #     cursor = conn.cursor()
        #     #파티멤버를 조회하는 sql문 실행해서 partymember로 저장
        #     with conn:
        #         with conn.cursor() as cur:
        #             cursor.execute(partymember_sql)
        #             partymember = cursor.fetchall()
        #             print(cut_select_charte)
        #             partymember_char_list =[]
        #             have_char_info_list=[]
        #             triger_num= 0
        #             for i in partymember:
        #                 partymember_char_list.append(i[0])
        #             for i in have_char_info:
        #                 have_char_info_list.append(i[0])
        #             for i in partymember_char_list:
        #                 if i in have_char_info_list:
        #                     triger_num=1
                        

        #     #만약 파티멤버에 나의 캐릭터가 존재하면 else 실행
        #             if have_char_info[0] in partymember_char_list:
        #                 QMessageBox.information(self,"바뻘","이미 선생님의 캐릭터가 신청되어있으셈")
        #             else:
        #                 cur.execute(cut_select_charte_sql, (select_party_num,cut_select_charte[0],cut_select_charte[1],cut_select_charte[2],login_my_id))
        #                 conn.commit()
        #             #파티자리 부분 리스트 제거
        #             self.view_partyseat_info.clear()
        #             cursor.execute(partymember_sql)
        #             #sql문 실행해서 새로운 파티멤버가 추가된 데이터를 가져옴
        #             partymember2 = cursor.fetchall()
        #             # 추가된 데이터를 파티자리 부분 리스트에 추가
        #             for i in partymember2:
        #                 print(i)
        #                 str_partymember= i[0]+"\n"+"Lv. "+ i[1] +"\n"+ i[2]
        #                 self.view_partyseat_info.addItem(str_partymember)
        #                 QMessageBox.information(self,"바뻘","신청 완료되썰")

        # except IndexError:
        #     QMessageBox.information(self,"바뻘","캐릭터 선택이 안되있지않셈")






#######################################################################################################


#######################################################################################################
#내가만든파티 부분
    #파티만들기 버튼
    def make_party_step(self):
        self.make_party_page = make_party.make_party_class()
        self.make_party_page.exec()
        #파티보이는 창 리셋
        self.view_party_info.clear()

        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
        cursor = conn.cursor()
        
        #파티 만들기창에서 파티 만들어 db에 입력하고 db에 접속해서 item을 다시 추가함
        view_party_sql = "select party_num,party_name,raid_name,party_startdate,party_starttime from party_table where party_startdate > (now()-INTERVAL 1 DAY) order by party_startdate, party_starttime"
        cursor.execute(view_party_sql)
        all_view_party_sql = cursor.fetchall()

        #내 파티 정보 가져오기
        view_my_party_sql="select party_num,party_name,raid_name,party_startdate,party_starttime from party_table where havechar_userinfo_userid = %s"%login.input_login_userid
        cursor.execute(view_my_party_sql)
        my_party_sql = cursor.fetchall()

        
        for i in all_view_party_sql:
            str_party= i[1]+"                                               "+str(i[0])+"\n"+i[2] +"\n"+i[3].isoformat()+"\n"+str(i[4])
            self.view_party_info.addItem(str_party)
        #내가 만든 파티정보 입력
        for i in my_party_sql:
            str_myparty= i[1]+"                                               "+str(i[0])+"\n"+i[2] +"\n"+i[3].isoformat()+"\n"+str(i[4])
            self.made_myparty_list.addItem(str_myparty)
            # print(str_party)


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