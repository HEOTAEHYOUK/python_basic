# tagnumber = int(input("조의 인원수를 입력하시오"))




# while tagnumber != 0:
#     name = input("이름을 입력하시오=")

#     number = input("번호를 입력하시오=")

#     email = input("이메일을 입력하시오=")

#     job = input("직업을 입력하시오=")

#     group = input("부서를 입력하시오=")

#     print("----------------------------------------------------------------------------")

#     print(("이름:")+   (name))

#     print(("번호:")+ (number))

#     print(("직업:")+    (job))

#     print(("부서:")+  (group))

#     print(("이메일:")+(email))

#     print("----------------------------------------------------------------------------")

#     if tagnumber: 5
#     first = [(name), (number), (job), (group), (email)]
#     if tagnumber: 4
#     second =[(name),(number), (job),(group), (email)]

#     tagnumber = tagnumber - 1 


# print(list(first),(second))

# 커밋 메세지를 뭘로 하는것이 좋을까? 
# 코드를 리뷰 후에 기입
# 
    
bcl = [()]

name = print(input("이름을 입력하시오"))

num = print(input("번호를 입력하시오"))

group = print(input("소속을 입력하시오"))


import sys
display = '''
---------------------------------------------------------
1.명함 입력, 2.명함수정, 3.명함삭제, 4.명함목록보기,5.종료 
---------------------------------------------------------
메뉴를 선택하세요 >>> '''

menu = ''
while True :
 menu = input(display)
 if menu == '1':
  print('명함입력')

  while True:
    email = input('')
    check = 0
    for index in range(len(card_list)):
     if card_list[index][3] == email:
      check = 1 
      break
     if check == 0:
      break
     card_list.append([name],[number],[group])
     print(card_list)

 elif menu == '2':
  print('명함수정')
  email = input('수정할 데이터 이메일 입력')
  check = 0
  for index in range(len(card_list)):
   if card_list[index][3] == email:
    check = 1
  while True:
   item = input('수정할 항목을 선택하세요(1.이름 2.전화번호, 3.주소, 4.종료)')
   if item == '4':
    break
   item = int(item-1)
   if item in(1,2,3):
    card_list[index][item] = input('수정할 값을 입력>>> ')
   


 elif menu == '3':
  print('명함삭제')
 elif menu == '4':
  print('명함목록보기')
 elif menu == '5':
  print('프로그램 종료')
  sys.exit()
 else:
  print('메뉴선택을 잘못하셨습니다')

#   이름 전화번호, 소속



