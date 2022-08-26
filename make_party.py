import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import main
import pymysql



def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.

#파티만들기창 ui 파일 연결
make_party_form = resource_path("./ui/make_party.ui")
make_party_form_class = uic.loadUiType(make_party_form)[0]



#파티만들기 창
class make_party_class(QDialog,QWidget,make_party_form_class):
    def __init__(self):
        super(make_party_class,self).__init__()
        self.initui()
        self.setWindowTitle('Party_make')

    def initui(self):
        self.setupUi(self)




#######################################################################################################
#날짜선택 부분
    def date_cho(self):

        #선택한 날짜를 Qdate 형식으로 가져옴
        cho_data = self.date_table.selectedDate()
        #Qdate형식의 변수를 문자열로 포메팅
        self.cho_date = cho_data.toString("yyyy-MM-dd")

        # 캘린더 아래 선택된 날자 텍스트로 보여줌
        self.view_date.setText(self.cho_date)
    


#######################################################################################################

#######################################################################################################
#시간 선택 부분
    def time_cho(self):
        # 선택한 시간을 qtime형식으로 가져옴
        time_data = self.time_table.time()
        #Qtime형식의 변수를 문자열로 포메팅
        self.cho_time = time_data.toString("hh:mm")

        self.view_time.setText(self.cho_time)

#파티이름 입력 부분
    def partyname_input(self):
        self.partyname_data = self.partyname_table.text()
        self.view_partyname.setText(self.partyname_data)



#######################################################################################################

#######################################################################################################
#정보입력 부분
    #난이도 선택 부분
    def difficulty_select(self):


        #select_difficulty 부분에서 선택된 난이도 값을 difficulty_value로 저장
        self.difficulty_value = self.select_difficulty.selectedItems()

        # 캐릭터 선택 리스트 초기화
        self.select_character.clear()

        # difficulty_value는 리스트 타입이기떄문에 text()함수 사용해서 이용        
        for item in self.difficulty_value:
            self.difficulty_value = item.text()

            self.party_info = self.raid_info + self.difficulty_value

            # 만약 선택된 self.raid_info값이 발탄이고 difficulty_value값이 노말 일떄 캐릭터레벨 1415이상의 캐릭터 정보 select_character list에 저장
            if self.raid_info == "발탄" and self.difficulty_value == "노말":
                for i in main.have_char_info:
                    if 1415 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 발탄이고 difficulty_value값이 하드나 헬 일떄 캐릭터레벨 1445이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "발탄" and self.difficulty_value in ["하드","헬"]:
                for i in main.have_char_info:
                    if 1445 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 비아키스이고 difficulty_value값이 노말 일떄 캐릭터레벨 1430이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "비아키스" and self.difficulty_value == "노말":
                for i in main.have_char_info:
                    if 1430 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 비아키스이고 difficulty_value값이 하드나 헬 일떄 캐릭터레벨 1460이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "비아키스" and self.difficulty_value in ["하드","헬"]:
                for i in main.have_char_info:
                    if 1460 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 쿠크세이튼이고 difficulty_value값이 노말 일떄 캐릭터레벨 1475이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "쿠크세이튼" and self.difficulty_value in ["노말","헬"]:
                for i in main.have_char_info:
                    if 1475 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 아브렐슈드이고 difficulty_value값이 노말 1~2 일떄 캐릭터레벨 1490이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "아브렐슈드" and self.difficulty_value == "노말 1~2":
                for i in main.have_char_info:
                    if 1490 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 아브렐슈드이고 difficulty_value값이 노말 1~4 일떄 캐릭터레벨 1500이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "아브렐슈드" and self.difficulty_value == "노말 1~4":
                for i in main.have_char_info:
                    if 1500 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 아브렐슈드이고 difficulty_value값이 노말 5~6 일떄 캐릭터레벨 1520이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "아브렐슈드" and self.difficulty_value == "노말 5~6":
                for i in main.have_char_info:
                    if 1520 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)   

            # 만약 선택된 self.raid_info값이 아브렐슈드이고 difficulty_value값이 하드 1~2 일떄 캐릭터레벨 1540이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "아브렐슈드" and self.difficulty_value == "하드 1~2":
                for i in main.have_char_info:
                    if 1540 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 아브렐슈드이고 difficulty_value값이 하드 1~4 일떄 캐릭터레벨 1550이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "아브렐슈드" and self.difficulty_value == "하드 1~4":
                for i in main.have_char_info:
                    if 1550 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)
            # 만약 선택된 self.raid_info값이 아브렐슈드이고 difficulty_value값이 하드 5~6 일떄 캐릭터레벨 1560이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "아브렐슈드" and self.difficulty_value == "하드 5~6":
                for i in main.have_char_info:
                    if 1560 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)    

            # 만약 선택된 self.raid_info값이 일리아칸이고 difficulty_value값이 노말 일떄 캐릭터레벨 1580이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "일리아칸" and self.difficulty_value == "노말":
                for i in main.have_char_info:
                    if 1580 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 일리아칸이고 difficulty_value값이 하드  일떄 캐릭터레벨 1600이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "일리아칸" and self.difficulty_value == "하드":
                for i in main.have_char_info:
                    if 1600 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)   

            # 만약 선택된 self.raid_info값이 카양겔이고 difficulty_value값이 노말 일떄 캐릭터레벨 1475이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "카양겔" and self.difficulty_value == "노말":
                for i in main.have_char_info:
                    if 1475 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 카양겔이고 difficulty_value값이 하드1 일떄 캐릭터레벨 1520이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "카양겔" and self.difficulty_value == "하드1":
                for i in main.have_char_info:
                    if 1520 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 카양겔이고 difficulty_value값이 하드2 일떄 캐릭터레벨 1560이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "카양겔" and self.difficulty_value == "하드2":
                for i in main.have_char_info:
                    if 1560 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)

            # 만약 선택된 self.raid_info값이 카양겔이고 difficulty_value값이 하드3 일떄 캐릭터레벨 1580이상의 캐릭터 정보 select_character list에 저장
            elif self.raid_info == "카양겔" and self.difficulty_value == "하드3":
                for i in main.have_char_info:
                    if 1580 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])  
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.party_info)                                             




    #레이드 선택 부분            
    def Legions_cho(self):
        #isChecked은 radio 요소를 선택했을떄 
        if self.valtan.isChecked():
            self.raid_info = "발탄"
            self.select_difficulty.clear()
            self.select_character.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("하드")
            self.select_difficulty.addItem("헬")

        elif self.bykas.isChecked():
            self.raid_info = "비아키스"
            self.select_difficulty.clear()
            self.select_character.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("하드")
            self.select_difficulty.addItem("헬")


        elif self.kakul_saydon.isChecked():
            self.raid_info = "쿠크세이튼"
            self.select_difficulty.clear()
            self.select_character.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("헬")

        elif self.brelshaza.isChecked():
            self.raid_info = "아브렐슈드"
            self.select_difficulty.clear()
            self.select_character.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말 1~2")
            self.select_difficulty.addItem("노말 1~4")
            self.select_difficulty.addItem("노말 5~6")
            self.select_difficulty.addItem("하드 1~2")
            self.select_difficulty.addItem("하드 1~4")
            self.select_difficulty.addItem("하드 5~6")


        elif self.kayanggel.isChecked():
            self.raid_info = "카양겔"
            self.select_difficulty.clear()
            self.select_character.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("하드1")
            self.select_difficulty.addItem("하드2")
            self.select_difficulty.addItem("하드3")

        elif self.akkan.isChecked():
            self.raid_info = "일리아칸"
            self.select_difficulty.clear()
            self.select_character.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("하드")







    #도전컨텐츠 클릭했을떄
    def challeng_content(self):
        if self.guardian.isChecked():

            self.raid_info = "도가토"
            #난이도부분과 캐릭터 부분 초기화
            self.select_difficulty.clear()
            self.select_character.clear()
            #선택한 컨텐츠를 즐길수 있는 래벨대의 캐릭터 부분에 추가
            for i in main.have_char_info:
                if 415 <=int(i[1]):
                    self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
            #선택한 파티정보 부분의 파티정보에 텍스트 추가
            self.view_raid.setText(self.raid_info)

        if self.abyss.isChecked():
            self.raid_info = "도비스"
            #난이도부분과 캐릭터 부분 초기화
            self.select_difficulty.clear()
            self.select_character.clear()
            #선택한 컨텐츠를 즐길수 있는 래벨대의 캐릭터 부분에 추가
            for i in main.have_char_info:
                if 415 <=int(i[1]):
                    self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
                self.view_raid.setText(self.raid_info)

        if self.rehearsal.isChecked():
            self.raid_info = "리허설"
            #난이도부분과 캐릭터 부분 초기화
            self.select_difficulty.clear()
            self.select_character.clear()
            #선택한 컨텐츠를 즐길수 있는 래벨대의 캐릭터 부분에 추가
            for i in main.have_char_info:
                if 1385 <=int(i[1]):
                    self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
            self.view_raid.setText(self.raid_info)

        if self.dejavu.isChecked():
            self.raid_info = "데자뷰"
            #난이도부분과 캐릭터 부분 초기화
            self.select_difficulty.clear()
            self.select_character.clear()
            #선택한 컨텐츠를 즐길수 있는 래벨대의 캐릭터 부분에 추가
            for i in main.have_char_info:
                if 1430 <=int(i[1]):
                    self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
            self.view_raid.setText(self.raid_info)

        if self.epidemic.isChecked():
            self.raid_info = "에피데믹"
            #난이도부분과 캐릭터 부분 초기화
            self.select_difficulty.clear()
            self.select_character.clear()
            #선택한 컨텐츠를 즐길수 있는 래벨대의 캐릭터 부분에 추가
            for i in main.have_char_info:
                if 1500 <=int(i[1]):
                    self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
                #선택한 파티정보 부분의 파티정보에 텍스트 추가
            self.view_raid.setText(self.raid_info)




    #캐릭터 선택 부분
    def char_cho(self):

        # 선택한 캐릭터을 가져옴
        self.char_data = self.select_character.currentItem().text()
        self.view_char.setText(self.char_data)
        













#######################################################################################################


#######################################################################################################
#선택한 파티정보 부분
    #만들기 버튼눌렀을떄 이벤트
    def make_btn(self):
        if self.view_date.text() == "":
            QMessageBox.information(self,"확인","날짜 선택이 안됬음 날짜 선택해주셈")
        elif self.view_time.text() == "":
            QMessageBox.information(self,"확인","시간 선택이 안됬음 시간 선택해주셈")
        elif self.view_raid.text() == "":
            QMessageBox.information(self,"확인","파티 선택이 안됬음 파티 선택해주셈")
        elif self.view_char.text() == "":
            QMessageBox.information(self,"확인","캐릭 선택이 안됬음 캐릭 선택해주셈")        
        else:
            if self.partyname_table.text() == "":
                self.partyname_data = "%s 님의 즐거운 %s 파티"%(main.login_my_topchar,self.view_raid.text())

            conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')

            cursor = conn.cursor()
            #선택한 파티정보의 데이터를 party_table에 추가하는 sql
            sql = "INSERT INTO `lostark`.`party_table` (`raid_name`, `party_name`, `havechar_userinfo_userid`, `havechar_charname`, `party_starttime`, `party_startdate`) VALUES (%s,%s,%s,%s,%s,%s);"
            #만들어진 파티정보 테이블과 보유 캐릭터 테이블을 조인해서 내가 입력한 캐릭터 정보를 가져오는 sql
            party_member_sql = """select max(party_num),havechar_charname,charlevel,charjob
                            from party_table a,havechar b
                            where a.havechar_charname = b.charname;"""
            #party_member_sql의 결과를 party_member테이블에 추가하는 sql
            input_member_sql = "INSERT INTO `lostark`.`party_member_table` (`party_table_party_num`, `party_member_charname`, `party_member_charlevel`, `party_member_charjob`,`userinfo_userid`) VALUES (%s, %s, %s, %s,%s);"


            set_view_char=self.view_char.text().split("  LV")
            with conn:
                with conn.cursor() as cur:
                    #선택한 파티정보의 데이터를 party_table에 추가
                    cur.execute(sql,(self.view_raid.text(), self.partyname_data, main.login_my_id, set_view_char[0], self.view_time.text(),self.view_date.text()))
                    conn.commit()

                    # 만들어진 파티정보 테이블과 보유 캐릭터 테이블을 조인해서 내가 입력한 캐릭터 정보를 가져옴
                    cursor.execute(party_member_sql)
                    party_member = cursor.fetchall()

                    #party_member_sql의 결과를 party_member테이블에 추가
                    cur.execute(input_member_sql,(party_member[0][0],party_member[0][1],party_member[0][2],party_member[0][3], main.login_my_id))
                    conn.commit()





            self.close()



#######################################################################################################

