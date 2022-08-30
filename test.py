import os
import sys


from PyQt5.QtWidgets import *
from PyQt5 import uic


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# #메인 화면 파일 연결
form = resource_path("./test.ui")
form_class = uic.loadUiType(form)[0]


class class_name(QDialog,QWidget, form_class):
    def __init__(self):
        super(class_name,self).__init__()
        self.initui()
    def initui(self):
        self.setupUi(self)
        #행만 추가
        self.tableWidget.setColumnCount(4)
        #테이블 수평정렬
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #행 header이름 변경
        table_column=["파티이름" , "종류,시간" , "공대장" , "인원 수"]
        self.tableWidget.setHorizontalHeaderLabels(table_column)

    #버튼누르면 테이블에 정보 추가
    def add_table(self):
        #버튼누르면 행 추가 
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        #
        party_name = "파티이름"
        party_value_time = "종류,시간"
        party_master = "공대장"
        party_member = "인원수"
        #numcols은 컬럼의 숫자를 카운트하는 columnCount() 함수로 현재 컬럼의 수 가져옴
        numcols = self.tableWidget.columnCount()
        #numrows은 열의 숫자를 카운트하는 rowCount()함수로 현재 열의 수를 가져옴
        numrows = self.tableWidget.rowCount()    
        #현재 열의 숫자만큼 세트
        self.tableWidget.setRowCount(numrows)
        #현재 컬럼의 숫자만큼 세트
        self.tableWidget.setColumnCount(numcols)
        #셀의 위치는 0에서부터 시작하기떄문에 현제 열의 숫자를 -1한 위치값에서 아이템 추가
        self.tableWidget.setItem(numrows -1,0,QTableWidgetItem(party_name))
        self.tableWidget.setItem(numrows -1,1,QTableWidgetItem(party_value_time))
        self.tableWidget.setItem(numrows -1,2,QTableWidgetItem(party_master))
        self.tableWidget.setItem(numrows -1,3,QTableWidgetItem(party_member))









        # #party_num 파티 개수

        # rowPosition = self.tableWidget.rowCount()
        # self.tableWidget.insertRow(rowPosition)

        # table_column=["파티이름" , "종류,시간" , "공대장" , "인원 수" , "신청하기"]
        # self.tableWidget.setHorizontalHeaderLabels(table_column)

        # party_name = "파티이름"
        # party_value_time = "종류,시간"
        # party_master = "공대장"
        # party_member = "인원수"
        # party_butten = "버튼"

        # # numcols = self.tableWidget.columnCount()
        # # numrows = self.tableWidget.rowCount()           
        # self.tableWidget.setRowCount(1)
        # self.tableWidget.setColumnCount(4)           
        # self.tableWidget.setItem(-1,0,QTableWidgetItem(party_name))
        # self.tableWidget.setItem(-1,1,QTableWidgetItem(party_value_time))
        # self.tableWidget.setItem(-1,2,QTableWidgetItem(party_master))
        # self.tableWidget.setItem(-1,3,QTableWidgetItem(party_member))
        # self.tableWidget.setItem( 1,4,QTableWidgetItem(party_butten))

        # self.tableWidget.setRowCount(numrows)

        # self.tableWidget.setColumnCount(numcols)
        # #컬럼 header
        # table_column=["파티이름" , "종류,시간" , "공대장" , "인원 수" , "신청하기"]
        # self.tableWidget.setHorizontalHeaderLabels(table_column)
        # qTableWidgetItemVar = QTableWidgetItem("호우")
        # qTableWidgetItemVar2 = QTableWidgetItem("호호우")
        
        # self.tableWidget.setItem(0,1,qTableWidgetItemVar)
        # self.tableWidget.setItem(0,2,qTableWidgetItemVar2)

        # item = self.tableWidget.item(1,1)
        
    # def add_guest(self):
    #     rowPosition = self.tableWidget.rowCount()
    #     self.tableWidget.insertRow(rowPosition)

    #     guest_name = self.lineEdit.text()
    #     guest_email = self.lineEdit_2.text()
        
    #     numcols = self.tableWidget.columnCount()
    #     numrows = self.tableWidget.rowCount()           
    #     self.tableWidget.setRowCount(numrows)
    #     self.tableWidget.setColumnCount(numcols)           
    #     self.tableWidget.setItem(numrows -1,0,QtGui.QTableWidgetItem(guest_name))
    #     self.tableWidget.setItem(numrows -1,1,QtGui.QTableWidgetItem(guest_email))
    #     print("guest added")   





if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = class_name()
    myWindow.show()
    app.exec_()