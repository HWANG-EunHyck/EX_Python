# -------------------------------------------------
# 함수(Function) 이해 및 활용
# -------------------------------------------------
# 함수 이름 : 3개의 정수를 입 덧셈한 후 결과를 반환하는 함수
# 함수 기능 : add3
# 매개 변수 : num1,num2,num3
# 함수 결과 : 정수 result
# -------------------------------------------------

def add3(*args):
    return int(sum(args))


# -------------------------------------------------
# 함수(Function) 이해 및 활용
# -------------------------------------------------
# 함수 이름 : 3개의 정수를 입 곱셈한 후 결과를 반환하는 함수
# 함수 기능 : multi3
# 매개 변수 : num1,num2,num3
# 함수 결과 : 정수 result
# -------------------------------------------------

# def add3(*args):
#     return args * args * args

# d = add3(1,2,3)

# print(d)

# -------------------------------------------------
# 함수(Function) 이해 및 활용
# -------------------------------------------------
# 함수 이름 : 2개의 정수를 나눗셈한 후 결과를 출력하는 함수
# 함수 기능 : div3
# 매개 변수 : num1,num2
# 함수 결과 : None
# -------------------------------------------------

def div(num1,num2):
    """ 이 함수는 리턴값이 없습니다."""
    if num2 != 0 :
        print(float(num1/num2))
    return None


## 함수 사용하기 즉 ,호출 ---------------------------
## 덧셈하기
value = add3(1,2,3)
print(value)
## 나눗셈하기
value1 = div(3,4)
