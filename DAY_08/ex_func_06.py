# --------------------------------------------------------------------
# 사용자 정의 함수
# --------------------------------------------------------------------
# 뎃셈, 뺄셈 , 나눗셈, 곱셈, 함수를 각각 만들기
# - 매개 변수 : 정수 2개, num1, num2
# - 함수 결과 : 연산 결과를 반환 

def add(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def gobhagi(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2 if num2 else '0으로 나눌수 없음'

# ---------------------------------------------------------------------
# 함수 기능 : 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수 이름 : check_data
# 매개 변수 : 문자열 데이터, 데이터 개수 data,count,sep=' '
# 함수 결과 : 유효 여부 True/False
# ---------------------------------------------------------------------

def check_data(data,count,sep=' '):
    # 데이터 여부
    if len(data):
    # 데이터 분리 후 갯수 체크
        data2 = data.split(sep)
        if count == len(data2): return True
        else:return False
    else:
        return False

print(check_data('+ 10 3',3))
print(check_data('+ 10',3))
print(check_data('+ 10 3 4',3))


# 함수 사용하기 즉, 호출 -----------------------------------------------
# [실습] 사용자로부터 연산자,숫자1,숫자2를 입력 받아서 연산 결과를 출력해주세요
#- input('연산자, 숫자1,숫자2 :').split(',')

a = input('연산자, 숫자1,숫자2 :').split(',')
giho = ['+','-',"/",'*']
if a[0] in giho:
    a[1] = int(a[1])
    a[2] = int(a[2])
    if a[0] == '+':
        print(add(a[1],a[2]))
    elif a[0] == '-':
        print(minus(a[1],a[2]))
    elif a[0] == '*':
        print(gobhagi(a[1],a[2]))
    elif a[0] == '/':
        print(divide(a[1],a[2]))
else:
    print('연산자가 아닙니다.')