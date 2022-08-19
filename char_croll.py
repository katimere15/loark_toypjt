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

print(result)

# #대표 캐릭터이름으로 보유하고있는 모든 캐릭터(charname) 데이터를 가져온다
# def return_havechar(address):
#     res = requests.get(address)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     charname_low = soup.select('#expand-character-list > ul > li > span > button > span')
#     charname=[]
#     #캐릭터명 
#     for i in charname_low:
#         charname.append(i.text)
#     return charname
# top_char=result[0][1]
# all_have_char=return_havechar("https://lostark.game.onstove.com/Profile/Character/%s" %top_char)
# print(all_have_char)



# #가지고 있는 캐릭터 직업(charjob) 데이터를 가져온다
# def return_charjob(address):
#     res = requests.get(address)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     charjob_low = soup.select('#expand-character-list > ul > li > span > button > img')
#     charjob=[]
#     #캐릭터 직업
#     charnum=len(charjob_low)
#     for j in range(charnum):
#         charjob.append(charjob_low[j]['alt'])
#     return charjob

# #캐릭터 레벨(charlev) 데이터를 가져온다.
# def return_charlevel(address):
#     res = requests.get(address)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     global lev_info
#     lev_info = soup.select_one('#lostark-wrapper > div > main > div > div.profile-ingame > div.profile-info > div.level-info2 > div.level-info2__expedition > span:nth-child(2)')
#     charlevel = lev_info.text
#     return charlevel

# print(result)




# result_data_cont = len(result)
# havechar_to_database=[]
# for i in range(result_data_cont):
#     charname=return_havechar("https://lostark.game.onstove.com/Profile/Character/%s" %result[i][1])
#     charjob=return_charjob("https://lostark.game.onstove.com/Profile/Character/%s" %result[i][1])
#     charname_count=len(charname)

#     for j in range(charname_count):
#         havechar_to_database.append(result[i][0])
#         havechar_to_database.append(charname[j])
#         char_level=return_charlevel("https://lostark.game.onstove.com/Profile/Character/%s" %charname[j])
#         havechar_to_database.append(char_level)
#         havechar_to_database.append(charjob[j])

#         sql = "INSERT INTO havechar (userinfo_userid,charname,charlevel,charjob) VALUES (%s, %s, %s ,%s)"
#         cursor.execute(sql, (havechar_to_database[0], havechar_to_database[1], havechar_to_database[2], havechar_to_database[3]))
#         conn.commit()

#         print(havechar_to_database)
        
#         havechar_to_database=[]





