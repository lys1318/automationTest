from datetime import datetime, timedelta

inputValue = 0
unitValue = 0
standard = 0

def commonUnit(inputValue):
    while inputValue < 1:
        print("1. 일수")
        print("2. 시간")
        print("단위 입력 : ", end='')
        unitValue = int(input())
        if unitValue == 1:
            print("경과되는 일수 입력 : ", end='')
            inputValue = int(input())
        elif unitValue == 2:
            print("경과되는 시간 입력 : ", end='')
            inputValue = int(input())
    return unitValue, inputValue

while standard < 1:
    print("1. 지정된 기간 기준")
    print("2. 현재시간 기준")
    print("기간 기준 입력 : ",end='')
    standard = int(input())
    if standard == 1:
        year, mon, day, hour = input("년,월,일,시간을 공백 문자로 구분하여 입력하세요 : ").split()
        year = int(year)
        mon = int(mon)
        day = int(day)
        hour = int(hour)
        unitValue, inputValue = commonUnit(inputValue)
    elif standard == 2:
        unitValue, inputValue = commonUnit(inputValue)

if (standard == 1) and (unitValue == 1):
    time = datetime(year,mon,day)
    print(time + timedelta(days = inputValue))
elif (standard == 1) and (unitValue == 2):
    time = datetime(year,mon,day,hour)
    print(time + timedelta(hours = inputValue))
elif (standard == 2) and (unitValue == 1):
    y, m, d = datetime.now().strftime('%Y %m %d').split()
    time = datetime(int(y),int(m),int(d))
    print (time + timedelta(days = inputValue))
elif (standard == 2) and (unitValue == 2):
    y, m, d, h, M, S = datetime.now().strftime('%Y %m %d %H %M %S').split()
    time = datetime(int(y),int(m),int(d),int(h),int(M),int(S))
    print (time + timedelta(hours = inputValue))