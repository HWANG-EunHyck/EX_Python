# ---------------------------------------------------
# 함수와 변수 - 지역/전역 변수
# ---------------------------------------------------
## 전역변수(Global Variable)--------------------------
## - 파일(py) 내에 존재하며 모든 곳에서 사용 가능
## - 프로그램 실행 시 메모리 존재
## - 프로그램 종료 시 메모리에서 삭제
## ---------------------------------------------------
total = 100

## 지역변수(Local Variable)
## - 함수(function) 내에 존재하며 함수에서만 사용 가능함!
## - 함수 실행 시 메모리 존재
## - 함수 종료 시 메모리에서 삭제 
## ---------------------------------------------------
# --------------------------------------------------------
# 함수 기능 : 정수를 덧셈한 후 결과를 반환하는 함수
# 함수 이름 : addint
# 매개 변수 : 0개~n개 즉, 가변인자
# 함수 결과 : 정수 result
# History : 
# ---------------------------------------------------------

def addint(*num):
    total = 0
    for n in num:
        total += n
    return total

# a = addint(1,2,5,7,9,10)
# print(a)
# print(total)

total = 100

def multiint(*num):
    total1 = 1
    for n in num:
        total1 *= n
    return total1+total

def multiint2(*num):
    # 전역변수의 값을 변경할 경우 그냥 사용 x
    global total
    for n in num:
        total *= n
    return total

## 함수 호출 ----------------------------------------------
result = addint(1)
print(f'result : {result}')

print(f'전 : total => {total}')
result2 = multiint2(5)
print(f'result2 : {result2}')

print(f'후 : total => {total}')