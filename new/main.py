import os
import sys
import login
import pymysql
import pandas as pd
import make_party
from PyQt5.QtWidgets import *
from PyQt5 import uic
import datetime

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# #메인 화면 파일 연결
main_form = resource_path("./ui/main.ui")
main_form_class = uic.loadUiType(main_form)[0]


class main_class(QDialog,QWidget, main_form_class):

    now_view_party_key = 0

    def __init__(self):
        super(main_class,self).__init__()
        self.initui()
        self.setWindowTitle('login')
    def initui(self):
        global login_myid

        global usercharter

        global usertopcharter

        global party_data

        


        self.setupUi(self)

        #로그인창에서 로그인 성공했을떄 id정보를 가져옴
        login_myid=login.input_login_userid
        usertopcharter = login.mytopcharter
        #가져온 로그인 id로 보유캐릭터 테이블에서 데이터 가져옴
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='party', charset='utf8')
        curs = conn.cursor()
        usercharter_sql = "select * from charter_table where userid ='%s'"%login_myid
        curs.execute(usercharter_sql)
        usercharter = curs.fetchall()
        
        #파티테이블에서 데이터 가져옴
        party_table_sql = "select * from party_table"
        curs = conn.cursor()
        curs.execute(party_table_sql)
        party_data = curs.fetchall()
        party_data_df = pd.DataFrame(party_data,columns=['파티키','만든유저아이디','공대장','파티이름','종류','시작시간'])

        # #맴버 테이블에서 내가 신청한 파티 데이터 가져옴
        # joinparty_sql = "select party_table_party_key from member_table where userid = '%s'"%login_myid
        # curs = conn.cursor()
        # curs.execute(joinparty_sql)
        # joinparty_key = curs.fetchall()
        # print(joinparty_key)

        #datetime.date타입의 지금 날짜,시간 데이터
        todaydata = pd.datetime.now()
        # party_data_df['시작시간'] = pd.to_datetime(party_data_df['Date'],format='%Y-%m-%d-%H-%M-%S')

        #출발하지않은 모든 파티데이터 
        all_party_data = party_data_df.loc[party_data_df['시작시간']>=todaydata].values.tolist()
        #출발 하루남은 파티 데이터
        todate_party_data = party_data_df.loc[party_data_df['시작시간'].between(todaydata, todaydata + datetime.timedelta(days=1))].values.tolist()
        #내가 만든 파티 데이터
        my_party_data = party_data_df.loc[(party_data_df['시작시간']>=todaydata) & (party_data_df['만든유저아이디']==login_myid)].values.tolist()

###########################################################################################################################################################################
        # 모든 파티 테이블
        #행만 추가
        self.all_partytable.setColumnCount(6)

        #수평 정렬
        self.all_partytable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #행header이름 변경
        table_column=["","파티이름" , "종류" , "파티만든 사람" , "시작 시간","파티 인원 보기"]
        self.all_partytable.setHorizontalHeaderLabels(table_column)

        #파티키 컬럼 숨기기
        self.all_partytable.setColumnHidden(0, True)


        for i in all_party_data:
            party_key = i[0]
            party_name = i[3]
            party_value = i[4]
            party_time = i[5].strftime("%m월 %d일 %H시 %M분")
            party_master = i[2]
            party_member = "인원수"


            #테이블안에 만들어질 버튼 시그널 연결
            self.member_check_btn = QPushButton("인원 보기")
            self.member_check_btn.clicked.connect(self.member_check_btn_signal)


            rowPosition = self.all_partytable.rowCount()
            self.all_partytable.insertRow(rowPosition)

            #numcols은 컬럼의 숫자를 카운트하는 columnCount() 함수로 현재 컬럼의 수 가져옴
            numcols = self.all_partytable.columnCount()
            #numrows은 열의 숫자를 카운트하는 rowCount()함수로 현재 열의 수를 가져옴
            numrows = self.all_partytable.rowCount()    
            #현재 열의 숫자만큼 세트
            self.all_partytable.setRowCount(numrows)
            #현재 컬럼의 숫자만큼 세트
            self.all_partytable.setColumnCount(numcols)
            #셀의 위치는 0에서부터 시작하기떄문에 행의 숫자를 -1한 위치값에서 아이템 추가
            self.all_partytable.setItem(numrows -1,0,QTableWidgetItem(str(party_key)))
            self.all_partytable.setItem(numrows -1,1,QTableWidgetItem(party_name))
            self.all_partytable.setItem(numrows -1,2,QTableWidgetItem(party_value))
            self.all_partytable.setItem(numrows -1,3,QTableWidgetItem(party_master))
            self.all_partytable.setItem(numrows -1,4,QTableWidgetItem(party_time))
            self.all_partytable.setCellWidget(numrows -1,5,self.member_check_btn)



        # 출발 하루남은 파티 테이블
        #행만 추가
        self.today_party_table.setColumnCount(6)

        #수평 정렬
        self.today_party_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #행header이름 변경
        table_column=["","파티이름" , "종류" , "파티만든 사람" , "시작 시간","파티 인원 보기"]
        self.today_party_table.setHorizontalHeaderLabels(table_column)

        #파티키 컬럼 숨기기
        self.today_party_table.setColumnHidden(0, True)


        for i in todate_party_data:
            party_key = i[0]
            party_name = i[3]
            party_value = i[4]
            party_time = i[5].strftime("%m월 %d일 %H시 %M분")
            party_master = i[2]
            party_member = "인원수"


            #테이블안에 만들어질 버튼 시그널 연결
            self.today_member_check_btn = QPushButton("인원 보기")
            self.today_member_check_btn.clicked.connect(self.today_member_check_btn_signal)


            rowPosition = self.today_party_table.rowCount()
            self.today_party_table.insertRow(rowPosition)

            #numcols은 컬럼의 숫자를 카운트하는 columnCount() 함수로 현재 컬럼의 수 가져옴
            numcols = self.today_party_table.columnCount()
            #numrows은 열의 숫자를 카운트하는 rowCount()함수로 현재 열의 수를 가져옴
            numrows = self.today_party_table.rowCount()    
            #현재 열의 숫자만큼 세트
            self.today_party_table.setRowCount(numrows)
            #현재 컬럼의 숫자만큼 세트
            self.today_party_table.setColumnCount(numcols)
            #셀의 위치는 0에서부터 시작하기떄문에 행의 숫자를 -1한 위치값에서 아이템 추가
            self.today_party_table.setItem(numrows -1,0,QTableWidgetItem(str(party_key)))
            self.today_party_table.setItem(numrows -1,1,QTableWidgetItem(party_name))
            self.today_party_table.setItem(numrows -1,2,QTableWidgetItem(party_value))
            self.today_party_table.setItem(numrows -1,3,QTableWidgetItem(party_master))
            self.today_party_table.setItem(numrows -1,4,QTableWidgetItem(party_time))
            self.today_party_table.setCellWidget(numrows -1,5,self.today_member_check_btn)





        # 내가 만든 파티 테이블
        #행만 추가
        self.mymakeparty_table.setColumnCount(6)

        #수평 정렬
        self.mymakeparty_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #행header이름 변경
        table_column=["","파티이름" , "종류" , "파티만든 사람" , "시작 시간","파티 인원 보기"]
        self.mymakeparty_table.setHorizontalHeaderLabels(table_column)

        #파티키 컬럼 숨기기
        self.mymakeparty_table.setColumnHidden(0, True)


        for i in my_party_data:
            party_key = i[0]
            party_name = i[3]
            party_value = i[4]
            party_time = i[5].strftime("%m월 %d일 %H시 %M분")
            party_master = i[2]
            party_member = "인원수"


            #테이블안에 만들어질 버튼 시그널 연결
            self.my_party_check_btn = QPushButton("인원 보기")
            self.my_party_check_btn.clicked.connect(self.my_party_check_btn_signal)


            rowPosition = self.mymakeparty_table.rowCount()
            self.mymakeparty_table.insertRow(rowPosition)

            #numcols은 컬럼의 숫자를 카운트하는 columnCount() 함수로 현재 컬럼의 수 가져옴
            numcols = self.mymakeparty_table.columnCount()
            #numrows은 열의 숫자를 카운트하는 rowCount()함수로 현재 열의 수를 가져옴
            numrows = self.mymakeparty_table.rowCount()    
            #현재 열의 숫자만큼 세트
            self.mymakeparty_table.setRowCount(numrows)
            #현재 컬럼의 숫자만큼 세트
            self.mymakeparty_table.setColumnCount(numcols)
            #셀의 위치는 0에서부터 시작하기떄문에 행의 숫자를 -1한 위치값에서 아이템 추가
            self.mymakeparty_table.setItem(numrows -1,0,QTableWidgetItem(str(party_key)))
            self.mymakeparty_table.setItem(numrows -1,1,QTableWidgetItem(party_name))
            self.mymakeparty_table.setItem(numrows -1,2,QTableWidgetItem(party_value))
            self.mymakeparty_table.setItem(numrows -1,3,QTableWidgetItem(party_master))
            self.mymakeparty_table.setItem(numrows -1,4,QTableWidgetItem(party_time))
            self.mymakeparty_table.setCellWidget(numrows -1,5,self.my_party_check_btn)





###########################################################################################################################################################################
        #파티인원 보기
    def member_check_btn_signal(self):
        self.member_list.clear()
        #클릭한 버튼 정보 가져오기
        cell_Position=self.sender()
        #버튼의 좌표값에 해당하는 셀 정보를 리턴
        cell_Position_Value = self.all_partytable.indexAt(cell_Position.pos())
        #위의 좌표값을 바탕으로 파티키 가져오기      
        btn_party_key = self.all_partytable.item(cell_Position_Value.row(),0).text()
        #지금 보고있는 파티의 파티키 전역변수에 대입
        global now_view_party_key
        now_view_party_key = btn_party_key
        #가져온 파티키로 db의 맴버테이블에 접근해서 정보 가져오기
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='party', charset='utf8')
        curs = conn.cursor()
        partymember_sql = "select charter_name,charter_level,charter_class from member_table where party_table_party_key = %s;"%btn_party_key
        curs.execute(partymember_sql)
        partymember = curs.fetchall()
        # 가져온 데이터 맴버리스트에 추가
        for i in partymember:
            partymember2 = " ".join(i)
            self.member_list.addItem(partymember2)

        party_value = self.all_partytable.item(cell_Position_Value.row(),2).text()
        main_class.select_cut(party_value,self)

        #출발하루남은 파티 파티인원 보기
    def today_member_check_btn_signal(self):
        self.member_list.clear()
        #클릭한 버튼 정보 가져오기
        cell_Position=self.sender()
        #버튼의 좌표값에 해당하는 셀 정보를 리턴
        cell_Position_Value = self.today_party_table.indexAt(cell_Position.pos())
        #위의 좌표값을 바탕으로 파티키 가져오기      
        btn_party_key = self.today_party_table.item(cell_Position_Value.row(),0).text()
        #지금 보고있는 파티의 파티키 전역변수에 대입
        global now_view_party_key
        now_view_party_key = btn_party_key
        #가져온 파티키로 db의 맴버테이블에 접근해서 정보 가져오기
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='party', charset='utf8')
        curs = conn.cursor()
        partymember_sql = "select charter_name,charter_level,charter_class from member_table where party_table_party_key = %s;"%btn_party_key
        curs.execute(partymember_sql)
        partymember = curs.fetchall()
        # 가져온 데이터 맴버리스트에 추가
        for i in partymember:
            partymember2 = " ".join(i)
            self.member_list.addItem(partymember2)

        party_value = self.today_party_table.item(cell_Position_Value.row(),2).text()
        main_class.select_cut(party_value,self)




        #내가만든 파티 인원 보기
    def my_party_check_btn_signal(self):
        self.member_list.clear()
        #클릭한 버튼 정보 가져오기
        cell_Position=self.sender()
        #버튼의 좌표값에 해당하는 셀 정보를 리턴
        cell_Position_Value = self.mymakeparty_table.indexAt(cell_Position.pos())
        #위의 좌표값을 바탕으로 파티키 가져오기      
        btn_party_key = self.mymakeparty_table.item(cell_Position_Value.row(),0).text()
        #지금 보고있는 파티의 파티키 전역변수에 대입
        global now_view_party_key
        now_view_party_key = btn_party_key
        #가져온 파티키로 db의 맴버테이블에 접근해서 정보 가져오기
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='party', charset='utf8')
        curs = conn.cursor()
        partymember_sql = "select charter_name,charter_level,charter_class from member_table where party_table_party_key = %s;"%btn_party_key
        curs.execute(partymember_sql)
        partymember = curs.fetchall()
        # 가져온 데이터 맴버리스트에 추가
        for i in partymember:
            partymember2 = " ".join(i)
            self.member_list.addItem(partymember2)

        party_value = self.mymakeparty_table.item(cell_Position_Value.row(),2).text()
        main_class.select_cut(party_value,self)

    def joinparty_btn(self):

        # 선택한 캐릭터 가져오기
        conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='party', charset='utf8')
        curs = conn.cursor()
        cho_char_str=self.charter_select.currentText()
        cho_char_str2 = cho_char_str.split()
        print(cho_char_str2)

        #파티 키 값과 유저 아이디를 기준으로 멤버테이블에 데이터가 있는지 없는지 체크
        joinmember_sql = "select charter_name,charter_level,charter_class,userid from member_table where party_table_party_key = '%s' and userid = '%s' ;"%(now_view_party_key,login_myid)
        curs.execute(joinmember_sql)
        joinmember = curs.fetchall()
        #멤버테이블에서 데이터를 못가져올때 insert
        if not joinmember:     
            joinmember_insert_sql = "INSERT INTO `party`.`member_table` (`party_table_party_key`, `charter_name`, `charter_level`, `charter_class`, `userid`) VALUES ('%s', '%s', '%s', '%s', '%s');"%(now_view_party_key,cho_char_str2[0],cho_char_str2[1],cho_char_str2[2],login_myid)
            curs.execute(joinmember_insert_sql)
            conn.commit()
            QMessageBox.information(self,"ok","완료되심")
        #멤버테이블에서 데이터를 발견했을때 메시지
        else:
            QMessageBox.information(self,"ok","이미 신청되있는거 아님 ??")




    def select_cut(party_value,self):
        for i in usercharter:
            if party_value in ["도비스","도가토"] and int(i[2])>=415:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "리허설" and int(i[2])>=1385:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "발탄노말" and int(i[2])>=1415:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value in ["비아키스노말","데자뷰"] and int(i[2])>=1430:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value in ["발탄하드","발탄헬"] and int(i[2])>=1445:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value in ["비아키스하드","비아키스헬"] and int(i[2])>=1460:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value in ["쿠크세이튼노말","쿠크세이튼헬"] and int(i[2])>=1475:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "아브렐슈드노말 1~2" and int(i[2])>=1490:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value in ["아브렐슈드노말 1~4","에피데믹"] and int(i[2])>=1500:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "아브렐슈드노말 5~6" and int(i[2])>=1520:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "아브렐슈드하드 1~2" and int(i[2])>=1540:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "아브렐슈드하드 1~4" and int(i[2])>=1550:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "아브렐슈드하드 5~6" and int(i[2])>=1560:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "일리아칸노말" and int(i[2])>=1580:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)
            elif party_value == "일리아칸하드" and int(i[2])>=1600:
                str_partyjoinchar= i[1]+" "+ i[2] +" "+ i[3]
                self.charter_select.addItem(str_partyjoinchar)




    def partymake_btn(self):
        self.close()
        self.make_party = make_party.make_party_class()
        self.make_party.show()
        #파티보이는 창 리셋
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = login.login_class()
    myWindow.show()
    app.exec_()