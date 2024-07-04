# ---------------------------------------------------
# 리스트 전용의 함수 즉, 메서드(method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
# ---------------------------------------------------
# [메서드 - 요소 순서 제어 메서드 reverse()]-------------

import random as ran

ran.seed(10) # 동일한 랜덤 숫자 추출을 위한 기준점
datas =[]
for i in range(10):
    datas.append(ran.randint(1,100))
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ') 

# datas : [74, 5, 55, 62, 74, 2, 27, 60, 63, 36]
print()
## 0번 => -1번으로 , -1 => 0번으로 위치 변경
datas.reverse()

print(f' datas : {datas}, datas 개수 : {len(datas)}개 ') 
print()
# [메서드 - 요소의 크기를 비교해서 정렬해주는 메서드 sort()]-------------
# - 기본 정렬 : 오름차순 즉, 작은 데이터부터 큰 데이터 순서로
datas.sort()
a =sorted(datas)

print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')
print(f' a     : {a}, a     개수 : {len(a)}개 ')

print()
datas.sort(reverse= True)
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')

# [메서드 - 리스트에서 요소를 꺼내는 메서드 pop()]-------------
# - 리시트에서 요소가 삭제됨

num = datas.pop()  # 제일 마지막 원소/요소
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')

num = datas.pop(0)  # 특정 인덱스의 원소/요소 꺼내기
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')
print()
# [메서드 - 리스트 확장 시켜주는 메서드 extend()]-------------
datas.extend([11,22,33,44])
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')

datas.extend((555,777)) # 리스트가 아니여도 넣어서 리스트의 요소로 만든다.
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')

datas.extend(('Good luck')) #요소를 다 쪼개서
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')

datas.extend({555,777,555,777}) # set이므로 중복은 빼고
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')

datas.extend({'name':'홍길동'}) # key 값만
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')
print()
# [메서드 - 모든 원소 삭제 메서드 clear()]-------------
datas.clear()
print(f' datas : {datas}, datas 개수 : {len(datas)}개 ')