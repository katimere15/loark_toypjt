import os
import sys
import pymysql
import requests
import login
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#회원가입 화면 파일 연결
signinwindow_form = resource_path("./ui/signinwindow.ui")
signinwindow_form_class = uic.loadUiType(signinwindow_form)[0]





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
    print(len(char_level)-3)
    char_level_set = char_level[3:len(char_level)-3]
    char_level_set2 = ''.join(char_level_set.split(","))
    char_job = soup.select_one("#lostark-wrapper > div > main > div > div.profile-character-info > img")["alt"]
    return char_name,char_level_set2,char_job

print(return_charlevel("https://lostark.game.onstove.com/Profile/Character/FoxNight"))

