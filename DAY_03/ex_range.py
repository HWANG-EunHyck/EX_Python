#-------------------------------------------------
# 내장함수 range()
# - 숫자 범위를 생성하는 내장함수
# - 형식 : range(시작숫자,끝숫자+1,간격)
#          range(끝숫자+1) : 0~끝 숫자
#-------------------------------------------------
# [실습1] 1~100 숫자를 저장하세요.
one = list(range(101))
print(type(range(101)), len(range(101)))
print()
print(one)
print()
# 원소/요소 읽기 ===> 인덱싱
print(range(101)[0], type(range(101)[0]))
print()
# 여러개 읽기 ==> 슬라이싱
print(range(101)[:30],type(range(101)[:30]))
print()
# 원소/요소 하나 하나 보기 ==> list 형변환
print(list(range(101)[:10]),tuple(range(101)[:10]))
print()
# [실습2] 1~100에서 3의 배수만 저장하세요

three = list(range(3,101,3))
print(three *3)
print()
# [실습3] 1.0 10.0의 사이에 숫자 저장
datas = list(range(1,11))
print(list(map(float,datas)))