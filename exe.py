from getUnivCal import getUnivCal
from saveCal import saveCal

# 용인예술과학대학교 웹사이트의 학사일정에서 일정 정보 크롤링
print("대학교 홈페이지에서 학사일정 불러오는중...")
scd = getUnivCal()

# saveCal(2024, 9, 4, "테스트")

# 일정에서 연, 월, 일, 일정내용을 추출한 2차원배열 scd
# scd의 인덱스 수 만큼 ics파일로 저장
print("일정 정보 저장 중..")
print("파일은 ics폴더 안에 저장됩니다.\n")
for s in scd:
    saveCal(int(s[0]), int(s[1]), int(s[2]), s[3])

print("\n\n실행완료")