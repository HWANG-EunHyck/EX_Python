#----------------------------------------------
# Dict 전용 함수 즉 ,메서드
# -> keys() valuse() items()
# ---------------------------------------------

person = dict(zip(['name','age'],['홍길동',10]))

d = person.items()

print(d)
print()

# [메서드 - 값 읽어오는 메서드 get(key)]---------
# - key에 해당하는 value가 없으면 default자리의 것 출력 일단 error가 안남
print(person['name'])

# print(person['gender']) Keyerror

print(person.get('name'))
print(person.get('gender','없음'))
print(person.get('gender'))
print()
# [메서드 - 수정 및 추가 메서드 update(k = v)]---------

person.update(gender = '남',job = '학생')
print(person)

person.update({'phone' : '010','birth' : '240102'})
print(person)

##**{'weight' : 100,'height' : 170}
## weight = 100,height170
person.update(**{'weight' : 100,'height' : 170})
print(person)