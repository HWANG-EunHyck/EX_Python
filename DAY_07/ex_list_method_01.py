# ---------------------------------------------------
# 리스트 전용의 함수 즉, 메서드(method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
# ---------------------------------------------------
import random as ran

# [1] 실습 데이터 => 임의의 정수 숫자 10개 구성된 리스트
# 
num = [7,3,9,11,3,7,2,1,8,4]

# [메서드 - 요소 인덱스를 반환하는 메서드 index()]
# -> 11의 인덱스를 찾기
# -> 왼쪽 >>>> 오른쪽으로 찾기
idx = num.index(11)
print(f'11의 인덱스 {idx}')

# -> 0의 인덱스를 찾기 => 존재하지 않는 데이터의 경우 ERROR
if 0 in num:
    idx = num.index(0)
    print(f'11의 인덱스 {idx}')
else:
    print(f'0은 원소로 존재하지 않습니다')
print()

# 3의 인덱스 찾기
num = [7,3,9,11,3,7,2,3,8,4]


if 3 in num:
    idx = num.index(3)
    print(f'첫번째 3의 인덱스 {idx}')
print()
if 3 in num:
    idx = num.index(3,2)
    print(f'두번째 3의 인덱스 {idx}')
print()
if 3 in num:
    idx = num.index(3,3)
    print(f'두번째 3의 인덱스 {idx}')


# [메서드 - 데이터가 몇개 존재하는지 갯수 파악하는 메서드 count(데이터)]
cnt = num.count(3)
print(f'3의 개수 : {cnt}개')
idx = 0
for i in range(cnt):
    idx = num.index(3,idx if not i else idx+1)
    print(f'{i+1}번째 3의 인덱스 : {idx}')