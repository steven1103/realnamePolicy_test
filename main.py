from bs4 import BeautifulSoup
import requests
from urllib import request
from variable import headers, bad_word

a=1;

#인터넷 실명제 전 후 제목 데이터 따오기

BASE_URL = 'https://gall.dcinside.com/board/lists/?id=news'
params = {
    'id' : 'news'
}

after_data = []
before_data = []

for i in range(10):
    before_list = ["49406","49407","49408","49409",'49410','49411','49412','49413','49414','49415']
    resp = requests.get(BASE_URL+'&page='+before_list[i], headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    contents = soup.find('tbody').find_all('tr')

    for a in contents:
        title_tag = a.find('a')
        title = title_tag.text
        before_data.append(title)

for s in range(10):
    after_list = ["49404", '49403',"49402","49401","49400",'49399','49398','49397','49396','49395']
    resp = requests.get(BASE_URL+'&page='+after_list[s], headers=headers)
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

print(str(count_af) + '/' + str(count_be))