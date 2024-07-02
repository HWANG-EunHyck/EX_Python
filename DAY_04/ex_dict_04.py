#-------------------------------------------------
# Dict 자료형 살펴보기
# - 연산자와 내장함수
#-------------------------------------------------

person ={'name':'홍길동','age': 20,"job":'학생'}
dog = dict(zip(['kind','weight','color','gender','age',],['cz','5kg','rainbow','female',25]))
jumsu  = {'국어': 100,'수학': 180,'체육': 77}

## [연산자] ---------------------------------------
# 산술 연산 x 
# person + dog 


# 멤버 연산자 : in ,not in
#       키
print('name' in dog)
# False
print('name' in person)
# True
print()
#       value      : dict 타입에서는 key만 멤버 연산자로 확인한다
# print('cz' in dog)
# # False
# print('20' in person)
# # False

# value 추출
print('cz' in dog.values())
print(20 in person.values())
print()

## [내장함수] ---------------------------------------
## - 원소/요소 개수 확인 : len()
print(f'dog의 요소 개수 : {len(dog)}개')
print(f'person의 요소 개수 : {len(person)}개')
print()

## - 원소/요소 정렬 : sorted() 
#  - 키만 정렬
print(f'dog의 오름차순정렬 : {sorted(dog)}')
print(f'dog의 내림차순정렬 : {sorted(dog,reverse = True)}')
print()
print(f'jumsu의 키의 오름차순정렬 : {sorted(jumsu)}')
print(f'jumsu의 값의 오름차순정렬 : {sorted(jumsu.values())}')
# jumsu의 오름차순정렬 : ['국어', '수학', '체육']
# jumsu의 오름차순정렬 : [77, 100, 180]
print(f'jumsu의 오름차순정렬 : {sorted(jumsu.items())}')
# jumsu의 오름차순정렬 : [('국어', 100), ('수학', 180), ('체육', 77)]
#                                                     ('국어',100)
print(f'jumsu의 오름차순정렬 : {sorted(jumsu.items(),key=lambda x:x[1],reverse = True) }')
 

# print(f'dog의 오름차순정렬 : {sorted(dog.values())}')
# 요소/원소가 동일한 타입일 경우에만 정렬이 가능함
