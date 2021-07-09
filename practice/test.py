# #모듈 삽입
from datetime import datetime, timedelta
# import os

# # #입력값 받기
# year, mon, day = input("년,월,일을 공백 문자로 구분하여 입력하세요 : ").split()
# year = int(year)
# mon = int(mon)
# day = int(day)
# # hour = int(hour)
# no_days = 0

# while no_days < 1:
#     print("%s년 %s월 %s일로부터 경과되는 일수를 입력하세요 : " %(year,mon,day),end='')
#     no_days = int(input())
# now = datetime.now()
# time = datetime(2018,9,5)
# print (now - time)

# time = datetime(year,mon,day,hour)
# print(time)



# for i in range(39930241,39930256):
#     if i%13 == 0:
#         print(i)
# from random import *
# fruits = ['apple', 'banana', 'orange']
# fruit = choice(fruits)
# word = ""

# print("answer : " + fruit)

# while True:
#     print()
#     success = True
#     for f in fruit:
#         if f in word:
#             print(f, end=" ")
#         else:
#             print("_", end=" ")
#             success = False
#     print("\n")

#     if success:
#         print("Success")
#         break

#     userInput = input("알파벳 입력 : ")
#     if userInput not in word:
#         word += userInput
    
#     if userInput in fruit:
#         print("Correct")
#     else:
#         print("Wrong")

# import sys
# sys.path.append("C:/python study/pc/pages/signUp.py")
# sys.path.append("/pc/tests")
# print(sys.path)

# def wonderFiScroll(self):
#     wonderFi = WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(MobileBy.ID("com.wemakeprice:id/v_wonder_filter")))
# 	wonderFiHeight = wonderFi.size
        
	# scroll.elPlusScroll(wonderFi, wonderFiHeight);

def operate (x, y):
    return x / y

print(operate (1,1))