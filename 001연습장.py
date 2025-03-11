

# name = input("이름을 입력하시오=")

# number = input("번호를 입력하시오=")

# email = input("이메일을 입력하시오=")

# job = input("직업을 입력하시오=")

# group = input("부서를 입력하시오=")

# print(("이름:")+   (name))

# print(("번호:")+ (number))

# print(("직업:")+    (job))

# print(("부서:")+  (group))

# print(("이메일:")+(email))

# (int(tagnumber)) > (int(tagnumber))

# -----------------------------------------------------------------------
#  주민등록 프로그램
# number = input("주민등록번호를 입력 하시오 >>> ")

# print(("생년월일>>>")+(number[0:6]))

# gender = number[7]

# if gender=='1' or gender=='3':
#     print("성별:남자")

# else:
#     print("성별:여자")

# a = number[0:8]
# b = ("******")

# print(a + b)

# -----------------------------------------------------------------------------
#  평균 내는 프로그램
# math = int(input("수학 점수를 입력하시오>>>"))

# eng = int(input("영어 점수를 입력하시오>>>"))

# avg = (math+eng)/2

# if avg >= 95:
#     print("등급: A+ \t점수: %.1f" %avg)

# elif avg >= 90:
#     print('등급: A\t점수:%.1f' %avg)

# -----------------------------------------------------------------------------

# ntn = int(input("사람수를 입력하시오"))

# while ntn != 0:
#     if ntn > 4:
#          name1 = input("이름을 입력하시오=")

#          number1 = input("번호를 입력하시오=")

#          email1 = input("이메일을 입력하시오=")

#          job1 = input("직업을 입력하시오=")

#          group1 = input("부서를 입력하시오=")

#          print("----------------------------------------------------------------------------")

#          print(("이름:")+   (name1))

#          print(("번호:")+ (number1))

#          print(("직업:")+    (job1))

#          print(("부서:")+  (group1))

#          print(("이메일:")+(email1))

#          print("----------------------------------------------------------------------------")

#          first = [(name1), (number1), (job1), (group1), (email1)]
#          ntn = (ntn - 1)
     
#     elif ntn > 3:
         
#          name2 = input("이름을 입력하시오=")

#          number2 = input("번호를 입력하시오=")

#          email2 = input("이메일을 입력하시오=")

#          job2 = input("직업을 입력하시오=")

#          group2 = input("부서를 입력하시오=")

#          print("----------------------------------------------------------------------------")

#          print(("이름:")+   (name2))

#          print(("번호:")+ (number2))

#          print(("직업:")+    (job2))

#          print(("부서:")+  (group2))

#          print(("이메일:")+(email2))

#          print("----------------------------------------------------------------------------")

#          second = [(name2), (number2), (job2), (group2), (email2)]

#          ntn = (ntn - 1)

#     elif ntn > 2:
         
#          name3 = input("이름을 입력하시오=")

#          number3 = input("번호를 입력하시오=")

#          email3 = input("이메일을 입력하시오=")

#          job3 = input("직업을 입력하시오=")

#          group3 = input("부서를 입력하시오=")

#          print("----------------------------------------------------------------------------")

#          print(("이름:")+   (name3))

#          print(("번호:")+ (number3))

#          print(("직업:")+    (job3))

#          print(("부서:")+  (group3))

#          print(("이메일:")+(email3))

#          print("----------------------------------------------------------------------------")

#          third = [(name3), (number3), (job3), (group3), (email3)]

#          ntn = (ntn - 1)

#     elif ntn > 1:
         
#          name4 = input("이름을 입력하시오=")

#          number4 = input("번호를 입력하시오=")

#          email4 = input("이메일을 입력하시오=")

#          job4 = input("직업을 입력하시오=")

#          group4 = input("부서를 입력하시오=")

#          print("----------------------------------------------------------------------------")

#          print(("이름:")+   (name4))

#          print(("번호:")+ (number4))

#          print(("직업:")+    (job4))

#          print(("부서:")+  (group4))

#          print(("이메일:")+(email4))

#          print("----------------------------------------------------------------------------")

#          forth = [(name4), (number4), (job4), (group4), (email4)]

#          ntn = (ntn - 1)

#     elif ntn > 0:
         
#          name5 = input("이름을 입력하시오=")

#          number5 = input("번호를 입력하시오=")

#          email5 = input("이메일을 입력하시오=")

#          job5 = input("직업을 입력하시오=")

#          group5 = input("부서를 입력하시오=")

#          print("----------------------------------------------------------------------------")

#          print(("이름:")+   (name5))

#          print(("번호:")+ (number5))

#          print(("직업:")+    (job5))

#          print(("부서:")+  (group5))

#          print(("이메일:")+(email5))

#          print("----------------------------------------------------------------------------")

#          fifth = [(name5), (number5), (job5), (group5), (email5)]

#          ntn = (ntn - 1)

#          list = print((first),(second),(third),(forth),(fifth),sep='\n')
# ---------------------------------------------------------
# mine = 10

# while mine > 0:
#     print('광물을 발견 했습니다')

#     mine = (mine -1)

#     if mine == 0:

#         print('더이상 광물이 없습니다')

#         break

# print(' 더 깊은 곳으로 이동합니다')

# dia = 5

# while dia > 0:

#     print('다이아를 발견 했습니다')

#     dia = (dia -1)

#     if dia == 0:

#         print('더이상 다이아가 없습니다')

import sys

display = '''
-------------------------------------------------------------
1. 도서 탐색, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

menu = ''

while True:
    menu = input(display)
    if menu == '1':
        print('도서탐색')
