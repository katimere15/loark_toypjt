import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import main



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
        self.cho_date = self.date_table.selectedDate()
        #Qdate로 형식의 cho_date를 문자로 변환해서 str_date에 대입
        self.str_date = self.cho_date.toString()
        #요일,월,일,연도순으로 되어있는 문자열 self.str_date을 연도,월,일,요일 순으로 정리
        self.lst_date = self.str_date.split()
        self.remove_date = self.lst_date[3],self.lst_date[1],self.lst_date[2]
        # YYYY-MM-DD순으로 정리된 변수
        self.set_date = '-'.join(self.remove_date)



        # 캘린더 아래 선택된 날자 텍스트로 보여줌
        self.view_cho_date.setText("선택된 날짜 : %s" %self.set_date)
        print(self.set_date)
        


#######################################################################################################


#######################################################################################################
#정보입력 부분
    #난이도 선택 부분
    def difficulty_select(self):
        #선택 레이드 종류데이터를 가져옴 
        Legions_value = self.raid_info

        #select_difficulty 부분에서 선택된 난이도 값을 difficulty_value로 저장
        difficulty_value = self.select_difficulty.selectedItems()

        # 캐릭터 선택 리스트 초기화
        self.select_character.clear()

        # difficulty_value는 리스트 타입이기떄문에 text()함수 사용해서 이용        
        for item in difficulty_value:
            difficulty_value = item.text()

            # 만약 선택된 Legions_value값이 발탄이고 difficulty_value값이 노말 일떄 캐릭터레벨 1415이상의 캐릭터 정보 select_character list에 저장
            if Legions_value == "발탄" and difficulty_value == "노말":
                for i in main.have_char_info:
                    if 1415 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 발탄이고 difficulty_value값이 하드나 헬 일떄 캐릭터레벨 1445이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "발탄" and difficulty_value in ["하드","헬"]:
                for i in main.have_char_info:
                    if 1445 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 비아키스이고 difficulty_value값이 노말 일떄 캐릭터레벨 1430이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "비아키스" and difficulty_value == "노말":
                for i in main.have_char_info:
                    if 1430 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
            # 만약 선택된 Legions_value값이 비아키스이고 difficulty_value값이 하드나 헬 일떄 캐릭터레벨 1460이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "비아키스" and difficulty_value in ["하드","헬"]:
                for i in main.have_char_info:
                    if 1460 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 쿠크세이튼이고 difficulty_value값이 노말 일떄 캐릭터레벨 1475이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "쿠크세이튼" and difficulty_value in ["노말","헬"]:
                for i in main.have_char_info:
                    if 1475 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 아브렐슈드이고 difficulty_value값이 노말 1~2 일떄 캐릭터레벨 1490이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "아브렐슈드" and difficulty_value == "노말 1~2":
                for i in main.have_char_info:
                    if 1490 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 아브렐슈드이고 difficulty_value값이 노말 1~4 일떄 캐릭터레벨 1500이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "아브렐슈드" and difficulty_value == "노말 1~4":
                for i in main.have_char_info:
                    if 1500 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 아브렐슈드이고 difficulty_value값이 노말 5~6 일떄 캐릭터레벨 1520이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "아브렐슈드" and difficulty_value == "노말 5~6":
                for i in main.have_char_info:
                    if 1520 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])     

            # 만약 선택된 Legions_value값이 아브렐슈드이고 difficulty_value값이 하드 1~2 일떄 캐릭터레벨 1540이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "아브렐슈드" and difficulty_value == "하드 1~2":
                for i in main.have_char_info:
                    if 1540 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 아브렐슈드이고 difficulty_value값이 하드 1~4 일떄 캐릭터레벨 1550이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "아브렐슈드" and difficulty_value == "하드 1~4":
                for i in main.have_char_info:
                    if 1550 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
            # 만약 선택된 Legions_value값이 아브렐슈드이고 difficulty_value값이 하드 5~6 일떄 캐릭터레벨 1560이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "아브렐슈드" and difficulty_value == "하드 5~6":
                for i in main.have_char_info:
                    if 1560 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])        

            # 만약 선택된 Legions_value값이 일리아칸이고 difficulty_value값이 노말 일떄 캐릭터레벨 1580이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "일리아칸" and difficulty_value == "노말":
                for i in main.have_char_info:
                    if 1580 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])
            # 만약 선택된 Legions_value값이 일리아칸이고 difficulty_value값이 하드  일떄 캐릭터레벨 1600이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "일리아칸" and difficulty_value == "하드":
                for i in main.have_char_info:
                    if 1600 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])     

            # 만약 선택된 Legions_value값이 카양겔이고 difficulty_value값이 노말 일떄 캐릭터레벨 1475이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "카양겔" and difficulty_value == "노말":
                for i in main.have_char_info:
                    if 1475 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 카양겔이고 difficulty_value값이 하드1 일떄 캐릭터레벨 1520이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "카양겔" and difficulty_value == "하드1":
                for i in main.have_char_info:
                    if 1520 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 카양겔이고 difficulty_value값이 하드2 일떄 캐릭터레벨 1560이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "카양겔" and difficulty_value == "하드2":
                for i in main.have_char_info:
                    if 1560 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])

            # 만약 선택된 Legions_value값이 카양겔이고 difficulty_value값이 하드3 일떄 캐릭터레벨 1580이상의 캐릭터 정보 select_character list에 저장
            elif Legions_value == "카양겔" and difficulty_value == "하드3":
                for i in main.have_char_info:
                    if 1580 <=int(i[1]):
                        self.select_character.addItem(i[0]+"  LV. "+i[1]+"  "+i[2])                                                




    #레이드 선택 부분            
    def Legions_btn(self):
        #isChecked은 radio 요소를 선택했을떄 
        if self.valtan.isChecked():
            self.raid_info = "발탄"
            self.select_difficulty.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("하드")
            self.select_difficulty.addItem("헬")
            # #선택한 레이드에 맞는 래벨대의 캐릭터 콤보박스에 추가
            # for i in main.have_char_info:
            #     if 1415 <=int(i[1]):
            #         self.select_difficulty.addItem(i[0]+"  LV. "+i[1])
        elif self.bykas.isChecked():
            self.raid_info = "비아키스"
            self.select_difficulty.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("하드")
            self.select_difficulty.addItem("헬")


        elif self.kakul_saydon.isChecked():
            self.raid_info = "쿠크세이튼"
            self.select_difficulty.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("헬")

        elif self.brelshaza.isChecked():
            self.raid_info = "아브렐슈드"
            self.select_difficulty.clear()
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
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("하드1")
            self.select_difficulty.addItem("하드2")
            self.select_difficulty.addItem("하드3")

        elif self.akkan.isChecked():
            self.raid_info = "일리아칸"
            self.select_difficulty.clear()
            #난이도 창에 난이도 추가    
            self.select_difficulty.addItem("노말")
            self.select_difficulty.addItem("하드")




    #보정컨탠츠
    def challenge_conten_btn(self):
        pass
        


    #결정하기 버튼 눌렀을때 이벤트
    def decide_info(self):
        pass







        #선택한 파티정보 부분으로 날릴 변수
        # date_info = self.set_date
        # raid_info = self.raid_info





#######################################################################################################


#######################################################################################################
#선택한 파티정보 부분
    #만들기 버튼눌렀을떄 이벤트
    def make_party(self):
        pass



#######################################################################################################

