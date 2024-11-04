from datetime import datetime
from os import path
from os import getcwd
from os import makedirs
import vobject

# 연 월 일 장소정보 파라미터
def saveCal(year=int,month=int,day=int,desc=str):

    scd = vobject.iCalendar()

    # 현재 시간
    curTime = datetime.now()
    # 일정 시작 (시간은 09시 20분 0초 고정)
    dayOn = datetime(year,month,day,9,20,0)
    # 일정 종료 (시간은 18시 30분 0초 고정)
    dayOff = datetime(year,month,day,18,30,0)

    vevent = scd.add('vevent')
    vevent.add('summary').value = desc
    vevent.add('description').value = desc
    vevent.add('dtstart').value = dayOn
    vevent.add('dtend').value = dayOff
    vevent.add('dtstamp').value = curTime
    vevent.add('location').value = "용인예술과학대학교" # 장소는 대학교 고정

    # ics폴더 아래에, 2024_09_03_동계.ics 등의 형식으로 iCalendar 파일 저장

    file = pathManager(dayOn.strftime("%Y_%m_%d_")+desc[:2]+".ics")
    with open(file, 'wb') as f:
        f.write(scd.serialize().encode('utf-8'))

# 운영체제 호환성 감안하여 ics폴더 생성 및 path관련 문제 조기소거
def pathManager(newFileName):
    icsPath = path.join(getcwd(), "ics")

    if not path.exists(icsPath):
        makedirs(icsPath)

    print(path.join(icsPath, newFileName))
    return path.join(icsPath, newFileName)