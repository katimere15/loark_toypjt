import requests
from bs4 import BeautifulSoup

#회원가입 화면에서 입력받은 대표캐릭터이름으로 가지고 있는 모든 캐릭터 이름 가져오는 함수
def return_all_havechar(address):
    res = requests.get(address)
    soup = BeautifulSoup(res.text, 'html.parser')
    charname_low = soup.select('#expand-character-list > ul > li > span > button > span')
    all_have_char=[]
    #캐릭터명 
    for i in charname_low:
        all_have_char.append(i.text)
    return all_have_char
# print(return_all_havechar("https://lostark.game.onstove.com/Profile/Character/SevenNight"))


    ############################################
    #캐릭터 이름과,레벨,직업 정보를 가져와 변수에 저장하는 함수
def return_charinfo(address):
    res = requests.get(address)
    soup = BeautifulSoup(res.text, 'html.parser')
    char_name = soup.select_one("#lostark-wrapper > div > main > div > div.profile-character-info > span.profile-character-info__name").text
    char_level = soup.select_one('#lostark-wrapper > div > main > div > div.profile-ingame > div.profile-info > div.level-info2 > div.level-info2__expedition > span:nth-child(2)').text
    char_level_set = char_level[3:len(char_level)-3]
    char_level_set2 = ''.join(char_level_set.split(","))
    char_job = soup.select_one("#lostark-wrapper > div > main > div > div.profile-character-info > img")["alt"]
    return char_name,char_level_set2,char_job