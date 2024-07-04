# ----------------------------------------------------
# 모  듈 : 변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지 : 동일한 목적의 모듈들을 모은 것
#         여러개의 모듈 파일들이 존재
# 모듈 사용법 : import 모듈파일명  <----- 확장자 제외
# ----------------------------------------------------
import random as ran


# # 임의의 숫자를 생성 추출 하기--------------------------
# # 임의의 숫자 10개 생성
# for i in range(10):
#     print(int(ran.random()*10))
# print()
# # -> randint(a,b) : a<=~<=b
# for i in range(10):
#     print(ran.randint(0,1))

## ------------------------------------
## [실습] 로또 프로그램을 만들어주세요.
## - 1~45 범위에서 중복되자 않는 6개 추출
## --------------------------------------

num = set()

while True:
    d = ran.randint(1,45)
    num.add(d)
    if len(num) >= 6  : break

print(num) 

lotto = [0,0,0,0,0,0]
idx = 0
while True:
    d = ran.randint(1,45)
    if d not in lotto:
        lotto[idx] = d
        idx += 1
    if idx == 6:break

print(lotto)

num = set()

while len(num) < 6 :
    d = ran.randint(1,45)
    num.add(d)

print(num) 

lotto = set()

while len(lotto)<6:
    d = ran.randint(1,45)
    num_set = set([d])
    lotto = lotto.union(num_set)

print(lotto)

# -----------------------------------------
# set 타입의 add()메서드

num = set()

while len(num) < 6 :
    d = ran.randint(1,45)
    num.add(d)

print(num)