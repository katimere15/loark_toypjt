# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\lostark_guild_pjt\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 807)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.choice_char_info = QtWidgets.QGroupBox(self.centralwidget)
        self.choice_char_info.setGeometry(QtCore.QRect(20, 190, 301, 541))
        self.choice_char_info.setObjectName("choice_char_info")

        self.char_cho = QtWidgets.QComboBox(self.choice_char_info)
        self.char_cho.setGeometry(QtCore.QRect(10, 20, 281, 21))
        self.char_cho.setObjectName("char_cho")

        self.widget = QtWidgets.QWidget(self.choice_char_info)
        self.widget.setGeometry(QtCore.QRect(20, 60, 261, 131))
        self.widget.setObjectName("widget")

        self.char_cho_name = QtWidgets.QLabel(self.widget)
        self.char_cho_name.setGeometry(QtCore.QRect(10, 60, 211, 31))
        self.char_cho_name.setObjectName("char_cho_name")

        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.char_cho_job = QtWidgets.QLabel(self.splitter)
        self.char_cho_job.setObjectName("char_cho_job")

        self.char_cho_level = QtWidgets.QLabel(self.splitter)
        self.char_cho_level.setObjectName("char_cho_level")

        self.gem_imprint = QtWidgets.QGroupBox(self.choice_char_info)
        self.gem_imprint.setGeometry(QtCore.QRect(20, 200, 261, 321))
        self.gem_imprint.setObjectName("gem_imprint")

        self.gam_info = QtWidgets.QListWidget(self.gem_imprint)
        self.gam_info.setGeometry(QtCore.QRect(10, 30, 111, 271))
        self.gam_info.setObjectName("gam_info")

        self.imprint_info = QtWidgets.QListWidget(self.gem_imprint)
        self.imprint_info.setGeometry(QtCore.QRect(140, 30, 111, 271))
        self.imprint_info.setObjectName("imprint_info")

        self.view_party = QtWidgets.QGroupBox(self.centralwidget)
        self.view_party.setGeometry(QtCore.QRect(350, 30, 281, 701))
        self.view_party.setObjectName("view_party")

        self.view_party_info = QtWidgets.QListWidget(self.view_party)
        self.view_party_info.setGeometry(QtCore.QRect(10, 50, 261, 601))
        self.view_party_info.setObjectName("view_party_info")

        self.cho_party_btn = QtWidgets.QPushButton(self.view_party)
        self.cho_party_btn.setGeometry(QtCore.QRect(190, 660, 75, 23))
        self.cho_party_btn.setObjectName("cho_party_btn")

        self.making_party_btn = QtWidgets.QPushButton(self.view_party)
        self.making_party_btn.setGeometry(QtCore.QRect(20, 660, 75, 23))
        self.making_party_btn.setObjectName("making_party_btn")

        self.view_partyseat = QtWidgets.QGroupBox(self.centralwidget)
        self.view_partyseat.setGeometry(QtCore.QRect(670, 30, 281, 701))
        self.view_partyseat.setObjectName("view_partyseat")

        self.view_partyseat_info = QtWidgets.QListWidget(self.view_partyseat)
        self.view_partyseat_info.setGeometry(QtCore.QRect(10, 90, 256, 561))
        self.view_partyseat_info.setObjectName("view_partyseat_info")

        self.cho_party_title = QtWidgets.QLabel(self.view_partyseat)
        self.cho_party_title.setGeometry(QtCore.QRect(20, 40, 241, 21))
        self.cho_party_title.setObjectName("cho_party_title")

        self.cho_partyseat_btn = QtWidgets.QPushButton(self.view_partyseat)
        self.cho_partyseat_btn.setGeometry(QtCore.QRect(190, 660, 75, 23))
        self.cho_partyseat_btn.setObjectName("cho_partyseat_btn")

        self.my_application = QtWidgets.QGroupBox(self.centralwidget)
        self.my_application.setGeometry(QtCore.QRect(990, 30, 281, 701))
        self.my_application.setObjectName("my_application")

        self.logininfo = QtWidgets.QGroupBox(self.centralwidget)
        self.logininfo.setGeometry(QtCore.QRect(20, 20, 301, 161))
        self.logininfo.setTitle("")
        self.logininfo.setObjectName("logininfo")

        self.hello_user = QtWidgets.QLabel(self.logininfo)
        self.hello_user.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.hello_user.setObjectName("hello_user")

        self.top_char = QtWidgets.QLabel(self.logininfo)
        self.top_char.setGeometry(QtCore.QRect(30, 60, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")

        font.setPointSize(16)
        self.top_char.setFont(font)
        self.top_char.setObjectName("top_char")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1292, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #텍스트 입력 함수
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #왼쪽
        self.hello_user.setText(_translate("MainWindow", "어서오십셔"))
        self.top_char.setText(_translate("MainWindow", "대표캐릭터 이름"))

        self.choice_char_info.setTitle(_translate("MainWindow", "선택 캐릭터"))
        self.char_cho_name.setText(_translate("MainWindow", "캐릭터명"))
        self.char_cho_job.setText(_translate("MainWindow", "직업이름"))
        self.char_cho_level.setText(_translate("MainWindow", "캐릭터레벨"))
        self.gem_imprint.setTitle(_translate("MainWindow", "보석 & 각인"))


        #가운데
        self.view_party.setTitle(_translate("MainWindow", "날짜_만들어진 파티"))
        self.cho_party_btn.setText(_translate("MainWindow", "선택"))
        self.making_party_btn.setText(_translate("MainWindow", "파티만들기"))


        self.view_partyseat.setTitle(_translate("MainWindow", "파티자리 확인"))
        self.cho_party_title.setText(_translate("MainWindow", "선택한 파티"))
        self.cho_partyseat_btn.setText(_translate("MainWindow", "신청"))

        #오른쪽
        self.my_application.setTitle(_translate("MainWindow", "신청한 파티 확인"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

