
import requests
from bs4 import BeautifulSoup
import pymysql

#데이터베이스 연결
conn = pymysql.connect(host='localhost', user='root', password='katimere1@', db='lostark', charset='utf8')
cursor = conn.cursor()

#sql 구문 
sql = "SELECT userid,top_char FROM userinfo"
cursor.execute(sql)

#데이터 검색(조회)
result = cursor.fetchall()
conn.close()

#대표 캐릭터이름으로 보유하고있는 모든 캐릭터(all_have_char) 데이터를 가져온다
def return_all_havechar(address):
    res = requests.get(address)
    soup = BeautifulSoup(res.text, 'html.parser')
    charname_low = soup.select('#expand-character-list > ul > li > span > button > span')
    all_have_char=[]
    #캐릭터명 
    for i in charname_low:
        all_have_char.append(i.text)
    return all_have_char


    #캐릭터 이름과,레벨,직업 정보를 가져와 변수에 저장한다.
def return_charlevel(address):
    res = requests.get(address)
    soup = BeautifulSoup(res.text, 'html.parser')
    char_name = soup.select_one("#lostark-wrapper > div > main > div > div.profile-character-info > span.profile-character-info__name").text
    char_level = soup.select_one('#lostark-wrapper > div > main > div > div.profile-ingame > div.profile-info > div.level-info2 > div.level-info2__expedition > span:nth-child(2)').text
    char_job = soup.select_one("#lostark-wrapper > div > main > div > div.profile-character-info > img")["alt"]
    return char_name,char_level,char_job

        
print(result)
user_count=len(result)
print(user_count)

for i in range(user_count):
    #대표캐릭터로 보유캐릭터 데이터 가져와 all_have_charname에 대입
    all_have_charname=return_all_havechar("https://lostark.game.onstove.com/Profile/Character/%s" %result[i][1])
    all_have_char_count=len(all_have_charname)
    #튜플로 가져온 all_have_charname 만큼 그 캐릭터의 이름,레벨,직업 정보를 가져온다.
    for j in range(all_have_char_count):
        char_info=[]
        char_info.extend([result[i][0],return_charlevel("https://lostark.game.onstove.com/Profile/Character/%s" %all_have_charname[j])])
        print(char_info)
        char_info=[]
    

