# -------------------------------------------------
# 함수(Function) 이해 및 활용
# -------------------------------------------------
# 함수 계반 계산기 프로그램
# 4칙 역산 기능별 함수 생성 => 덧셈,뺄셈,곱셈,나눗셈
# 2개 정수만 계산
# -------------------------------------------------

def plus(a,b):
    a= str(a)
    b= str(b)
    if a.isnumeric() and b.isnumeric():
        result =int(a)+int(b)
        return result
    else:
        result ='숫자가 아닙니다'
        return result

def minus(a,b):
    a= str(a)
    b= str(b)
    if a.isnumeric() and b.isnumeric():
        result =int(a)-int(b)
        return result
    else:
        result ='숫자가 아닙니다'
        return result

def div(a,b):
    a= str(a)
    b= str(b)
    if a.isnumeric() and b.isnumeric():
        if b != '0':
            result =int(a)/int(b)
            return result
        else:
            result ='0은 나눌수 없습니다'
            return result
    else:
        result ='숫자가 아닙니다'
        return result

def multi(a,b):
    a= str(a)
    b= str(b)
    if a.isnumeric() and b.isnumeric():
        result =int(a)*int(b)
        return result
    else:
        result ='숫자가 아닙니다'
        return result

# 메뉴 출력 함수--------------------------------------------
# 함수 기능 : 계산기 메뉴를 출력하는 함수
# 함수 이름 : print_menu()
# 매개 변수 : 없음
# 함수 결과 : 없음
# ---------------------------------------------------------
def print_menu():
    print(f'{"*":*^16}')
    print(f'{"계 산 기":^14}')
    print(f'{"*":*^16}')
    print(f'{"*  1. 덧  셈   *":^14}')
    print(f'{"*  2. 뺄  셈   *":^14}')
    print(f'{"*  3. 나눗셈   *":^14}')
    print(f'{"*  4. 곱  셈   *":^14}')
    print(f'{"*  5. 종  료   *":^14}')
    print(f'{"*":*^16}')

# print_menu()

# ----------------------------------------------------------
# 함수 기능 : 연산 수행 후 결과를 반환하는 함수
# 함수 이름 : cal()
# 매개 변수 : 함수명, str 숫자2개 ,str 연산자 기호
# 함수 결과 : 
# ---------------------------------------------------------
def cal(func,num1,num2,op):
    print(f'결과: {num1} {op} {num2} = {func(num1,num2)}')

# a= plus(5224,3241)
# b = minus(3242,5412)
# c= multi(111,9)
# d = div(142,744)
# d_ = div(5,0)

# --------------------------------------------------
# - 사용자 종료를 원할떄 종류 => 'x', 'X' 입력 시
# - 계산 연산방식과 숫자 데이터 입력 받기
# --------------------------------------------------

# while True:
#     #1 입력 받기
#     req = input('연산(+,-,/,*) 방식과 정수 2개 입력 (예: + 10 2)')
#     #2 종료 조건 검사
#     if req == 'x' or req =='X':
#         print('계산기를 종료합니다')
#         break
#     #3 입력에 연산방식과 데이터 추출
#     op,num1,num2 = req.split()
#     if op == "+":
#         print(plus(num1,num2))
#     elif op == '-':
#         print(minus(num1,num2))
#     elif op == '/':
#         print(div(num1,num2))
#     elif op == '*':
#         print(multi(num1,num2))
#     else:
#         print('올바른 연산자가 아닙니다')

## 계산기 프로그램 ------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴 출력
# - 종료 메뉴 선택 시 프로그램 종료
# => 반복 ---> 무한 반복 : while
## ---------------------------------------------------
cnt =0
while True:  
    # 메뉴 출력
    print_menu()
    

    # 메뉴 선택 요청
    choice = input('메뉴 선택:')
    if choice.isdecimal():
         choice = int(choice)
    else:
         print('숫자만 입력하세요')
         continue
    
    if cnt>1:
        print('3회 잘못입력하셨습니다.')
        break
         # 종료 조건(5번 메뉴 선택) 처리
    if choice ==5:
            print('프로그램을 종료합니다')
            break
    elif choice ==1: # 덧셈
            print('덧셈')
            num1,num2 = input().split()
            cal(plus,num1,num2,'+')
    elif choice ==2: # 덧셈
            print('뺄셈')
            num1,num2 = input().split()
            cal(minus,num1,num2,'-')
    elif choice ==3: # 덧셈
            print('곱셈')
            num1,num2 = input().split()
            cal(multi,num1,num2,'*')
    elif choice ==4: # 덧셈
            print('나눗셈')
            num1,num2 = input().split()
            cal(div,num1,num2,'/')
    else: 
            print('선택된 메뉴는 없습니다.\n')
            cnt+=1

   
