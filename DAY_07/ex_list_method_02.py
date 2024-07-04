# ---------------------------------------------------
# 리스트 전용의 함수 즉, 메서드(method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
# ---------------------------------------------------
# [메서드 - 요소 추가 메서드 append(데이터)]

datas =[1,3,5]

# 새로운 데이터 100 추가
datas.append(100)
print(f'datas 개수 : {len(datas)}개 {datas})')

datas.append(100)
print(f'datas 개수 : {len(datas)}개 {datas})')

# [메서드 요소 추가 메서드 insert(인덱스,데이터)]--------
datas.insert(0,300)
print(f'datas 개수 : {len(datas)}개 {datas})')

datas.insert(-1,300) #=> 무조건 있던 자리에 있던 친구가 뒤로 한칸 밀린다.
print(f'datas 개수 : {len(datas)}개 {datas})')

# [메서드 요소 추가 메서드 insert(인덱스,데이터)]--------

#[실습] 임의의 정수 숫자 10개 저장하는 리스트 생성-------

import random as ran

num =[]
for i in range(10):
    num.append(ran.randint(1,100))
print(f'num의 개수 : {len(num)}개 , num : {num}') 


# [메서드 - 요소 삭제 메서드 remove(데이터)]
# num : [9, 92, 59, 34, 52, 46, 1, 83, 90, 25]
# - 존재하지 않는 데이터 삭제 시 ERROR 발생함!
num.remove(1)
print(f'num의 개수 : {len(num)}개 , num : {num}') 