#-------------------------------------------------
#  set 자료형 살펴보기 (중복제거용)
# - 연산자
#-------------------------------------------------
d1 = {1,3,5,7}
d2 = {1,2,4,6,8}

## 덧셈연산 ==> 메서드 사용 : 합집합
# print(d1+d2)
#==> 불가능
print( d1.union(d2), d1|d2 )

## 공통 원소 ==> 교집합
print( d1.intersection(d2), d1&d2 )

## 차집합 ==> 공통 원소 제외한 나머지
print( d2.difference(d1), d1-d2 )
