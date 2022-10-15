from bs4 import BeautifulSoup
import requests
from urllib import request
from variable import headers, bad_word

a=1;

#인터넷 실명제 전 후 제목 데이터 따오기

t = input("몇개의 게시글을 분석하시겠습니까? (단위 : 20)")
t = int(t)
BASE_URL = 'https://gall.dcinside.com/board/lists/?id=news'
params = {
    'id' : 'news'
}

after_data = []
before_data = []

for i in range(t):
    page_number = str(49406+i)
    resp = requests.get(BASE_URL+'&page='+page_number, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    contents = soup.find('tbody').find_all('tr')

    for a in contents:
        title_tag = a.find('a')
        title = title_tag.text
        before_data.append(title)

for s in range(t):
    page_number = str(49404-s)
    resp = requests.get(BASE_URL+'&page='+page_number, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    contents = soup.find('tbody').find_all('tr')

    for a in contents:
        title_tag = a.find('a')
        title = title_tag.text
        after_data.append(title)

#욕설 판단 메커니즘

count_be = 0
count_af = 0

for n in range(len(after_data)):
    for a in range (len(bad_word)):
        if bad_word[a] in after_data[n]:
            count_af += 1

for m in range(len(before_data)):
    for b in range (len(bad_word)):
        if bad_word[b] in before_data[m]: 
            count_be += 1

print("이전 욕설 수치" + str(count_be))
print("이후 욕설 수치" + str(count_af))

def compare(count_be, count_af):
    if count_be < count_af:
        try: value = round((count_af - count_be) / count_be * 100, 2)
        except : value = 100
    elif count_be > count_af:
        try:value = -round((count_be-count_af)/count_be* 100/2)
        except: value = -100
    else:
        value = 0
    return value

var = compare(count_be=count_be, count_af=count_af)
if var > 0:
    print("증가율 : " + str(var) + "%")
elif var < 0:
    print("감소율" + str(var) + "%")
else: 
    print("증감 없음")

