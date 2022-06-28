from calendar import month
from datetime import datetime
import datetime
import numpy as np

# 8자리 시작, 마지막 날짜 입력
startDate = "20231227"
lastDate = "20220106"

# 각 날짜를 리스트에 끊어서 저장
# ex) 20220627 = ['2', '0', '2', '2', '0', '6', '2', '7']
start_dateList = []
for y in (startDate):
    start_dateList.append(y)
last_dateList = []
for y in (lastDate):
    last_dateList.append(y)

# string 타입의 리스트를 int 타입으로 변환
start_dateList = list(map(int, start_dateList))
last_dateList = list(map(int, last_dateList))

# 시작 날짜 정리
thousand = start_dateList[0] * 1000
hundred = start_dateList[1] * 100
yten = start_dateList[2] * 10
yone = start_dateList[3]
mten = start_dateList[4] * 10
mone = start_dateList[5]
dten = start_dateList[6] * 10
done = start_dateList[7]
startYear = thousand + hundred + yten + yone
startMonth = mten + mone
startDay = dten + done

# 마지막 날짜 정리
thousand = last_dateList[0] * 1000
hundred = last_dateList[1] * 100
yten = last_dateList[2] * 10
yone = last_dateList[3]
mten = last_dateList[4] * 10
mone = last_dateList[5]
dten = last_dateList[6] * 10
done = last_dateList[7]
lastYear = thousand + hundred + yten + yone
lastMonth = mten + mone
lastDay = dten + done

# datetime으로 적용
startday = datetime.date(startYear, startMonth, startDay)
lastday = datetime.date(lastYear, lastMonth, lastDay)

# 두 날짜간 차이 계산
dateResult = startday - lastday
dateResult = abs(dateResult)

# 날짜형 -> 문자형 변환 후 날짜간 차이를 정수형으로 저장
strDate = str(dateResult)
sstrDate = strDate.split(' ')
intDate = int(sstrDate[0])      # 날짜간 차이(정수형)

monthList = []      # 사용자가 지정한 month의 리스트
dateList = []       # 사용자가 지정한 day의 리스트

#   1월 2월 3월 4월  5월 6월 7월 8월 9월 10월 11월 12월
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,  30,  31]

# 같은 달일때
if startMonth == lastMonth and intDate < m[startMonth-1] :
    for i in range(startDay,lastDay+1) :
        dateList.append(i)
        monthList.append(startMonth)
# 다른 달일때
elif startMonth != lastMonth :
    # 다른 연도
    if startYear != lastYear :
        m_m = lastMonth - startMonth
        m_m = abs(abs(m_m)-12)+1
        for i in range(m_m) :
            if i == 0 :
                for j in range(startDay,m[((startMonth-1)+i)-12]+1):
                    dateList.append(j)
                    monthList.append((startMonth-1)+i+1)
            elif 0<i<m_m-1:
                for j in range(1,m[((startMonth-1)+i)-12]+1):
                    dateList.append(j)
                    monthList.append(i)
            else :
                for j in range(1,lastDay+1):
                    dateList.append(j)
                    monthList.append(i)            
    # 같은 연도
    else :
        m_m = lastMonth - startMonth +1
        for i in range(m_m) :
            if i == 0 :
                for j in range(startDay,m[startMonth-1]+1):
                    dateList.append(j)
                    monthList.append(startMonth)
            elif 0<i<m_m-1:
                for j in range(1,m[startMonth-1+i]+1):
                    dateList.append(j)
                    monthList.append((startMonth-1)+1)
            else :
                for j in range(1,lastDay+1):
                    dateList.append(j)
                    monthList.append((lastMonth-1)+1)

# 정수형 리스트를 문자열 리스트로 변환
str_month_list = list(map(str, monthList))
str_date_list = list(map(str, dateList))

# n월 n일 형태로 출력
listLen = len(str_month_list)
resultList = []
for i in range(listLen):
    resultList.append(str_month_list[i] + "월 " + str_date_list[i] + "일")

print(resultList)