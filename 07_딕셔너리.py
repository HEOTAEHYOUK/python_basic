name_card = {'name':'홍길동',
              'tel':'010-0000-0000',
              'adress':'부산',
              'email':'hong@gmail.com' }

print(name_card)

name_card['etc'] =  ['이사 갈수도 있음','1년안에']#키 값은 대괄호 사용하여 사용, 키값 주의해서 사용

print(name_card)

print(name_card['adress'])

print(name_card['etc'][1])

del name_card['adress']

print(name_card)

print(type(name_card))  #딕테이셔너리 값

print(len(name_card))

# print(name_card['adress']) 없는 값을 사용해서 오류

print('adress' in name_card) 

print(name_card.keys())  # 괄호 사용시 함수가 됨됨

print(name_card.values())

print(name_card.items())
print('---------------------------------------------')
for k in name_card.keys(): 
    print(k)

print('---------------------------------------------')

for k in name_card.values():
    print(k)

print('---------------------------------------------')

for k,v in name_card.items():
    print(k,v)

name_card.clear()  #딕셔너리를 비워줌

print(name_card)


print(name_card.get('address'))  #오류를 발생시키고 싶지 않을때 get 사용


s1 = set([1,2,3,3,2]) #덮어 씌움 
print(s1)

s2 = set('hello')  #순서가 없기 때문에 무작위 출력

print(s2)