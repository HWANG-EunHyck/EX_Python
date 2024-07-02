# ----------------------------------------------------------
# 조건부 표현식
# ----------------------------------------------------------
## [실습] 임의 숫자가 5의 배수 여부 결과를 출력하세요 
#         

# num = int(input())

# print('5의 배수') if not num%5 else print('5의 배수 아님')

## [실습] 문자열을 입력받아서 문자열의 원소 개수를 저장
## - 단 원소 개수가 0 이면 None 저장

# alp = input()

# # if len(alp) :
# #     result = len(alp)
# # else:
# #     result = None

# result = len(alp) if len(alp) else None 

# print(result)

## [실습] 연산자(사칙연산자: +,-,*,/)와 숫자 2개 입력 받기
## - 입력된 연산자에 따라 계산 결과 저장
## - 예) 입력 : + 10 3  출력 : 13

cal = input('입력 : ').split()

if cal[0] == '+' :
    print(int(cal[1])+int(cal[2]))
elif cal[0] == '-' :
    print(int(cal[1])-int(cal[2]))
elif cal[0] == '*' :
    print(int(cal[1])*int(cal[2]))
elif cal[0] == '/' :
    print(int(cal[1])/int(cal[2]))
else:
    print('잘못된 입력')