import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt

# 용인예술과학대학교 학사일정 불러오기
# [[연, 월, 일, 내용],[연, 월, 일, 내용]] 형식의 2차원 배열
def getUnivCal():

    year = dt.now().year
    month = 1
    day = 1
    desc = ""

    # 대학 학사일정 사이트
    url = 'https://www.ysc.ac.kr/kor/CMS/ScheduleMgr/MonthList.do?mCode=MN088&calendar_year='+str(year)+'&calendar_month='

    # 크롤링 한 정보를 저장할 배열
    scd = []

    while month < 13 :
        source = requests.get(url+str(month))
        soup = bs(source.content, 'lxml')

        for t in soup.find_all('td'):
            if(t.find('li') is not None): # 일정이 있는 날의 경우 ul태그는 있으나 li태그는 없음
                day = t.find('div', class_='day-tit').text
                    
                for li in t.find_all('li'):
                    desc = li.text
                    scd.append([str(year), str(month), day, desc])

        month+=1

    # print(scd)

    print("**********")
    print(scd[0])
    print(scd[-1])
    print("**********\n")

    return scd