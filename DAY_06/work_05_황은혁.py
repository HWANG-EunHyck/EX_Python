# i = 0 
# while i<100:
#     print('hello world!', i)
#     i += 1
# print()

# i = 100
# while i>0:
#     print('hello world!',i)
#     i -= 1

# count = int(input('숫자를 입력하세요'))


# # while count >0:
# #     print('hello world', count)
# #     count -= 1

# i = 0
# while i < count:
#     print('hello world', i)
#     i += 1

import random

# print(random.random())
# print(random.random())
# print(random.random())
# 0.6184315524828503
# 0.7776745195639267
# 0.26375845168610335

# print(random.randint(1,6))
# print(random.randint(1,6))
# print(random.randint(1,6))
# 1
# 3
# 3

# i = 0
# while i != 3:
#     i = random.randint(1,6)
#     print(i)

# dice = [1,2,3,4,5,6]

# print(random.choice(dice))
# print(random.choice(dice))
# print(random.choice(dice))

# print(random.randint(1,6))

# dice = ['1','fff','ddd',2,'gggg']

# print(random.choice(dice))

# i = 0
 
# while i < 20:
#      print('Hello, world!',i)
#      i = i + 2

# 17.5 연습문제: 변수 두 개를 다르게 반복하기
# 다음 소스 코드를 완성하여 정수 2 5, 4 4, 8 3, 16 2, 32 1이 각 줄에 출력되게 만드세요.
# while에 조건식은 두 개 지정하고, 두 변수를 모두 변화시켜야 합니다.

# i = 2
# j = 5

# # 2 5
# # 4 4
# # 8 3
# # 16 2
# # 32 1

# while i<= 32 or j>0:
#     print(i , j)
#     i *= 2
#     j -= 1

# 17.6 심사문제: 교통카드 잔액 출력하기
# 표준 입력으로 금액(정수)이 입력됩니다. 1회당 요금은 1,350원이고, 
# 교통카드를 사용했을 때마다의 잔액을 각 줄에 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 최초 금액은 출력하지 않아야 합니다. 그리고 잔액은 음수가 될 수 없으며 잔액이 부족하면 출력을 끝냅니다.

# 입력
# 10000
# 결과
# 8650
# 7300
# 5950
# 4600
# 3250
# 1900
# 550

# i = int(input())

# while i>=1350:
#     i = i-1350
#     print(i)

# if i >= 0:
#     while i>=0:
#         i = i-1350
#         print(i)
# else: None


# i = 0

# while True:
#     print(i)
#     i += 1
#     if i == 100:
#         break

# for i in range(100000):
#     print(i)
#     if i == 100:
#         break

# for i in range(30):
#     if i%2 == 0:
#         continue
#     print(i)

# i = 0 
# while i <30:
#     i += 1
#     if i%2 == 0:
#         continue
#     print(i)

# count = int(input())

# i=0
# while True:
#     print(i)
#     i +=1
#     if i == count:
#         break

# 18.5 연습문제: 3으로 끝나는 숫자만 출력하기
# 다음 소스 코드를 완성하여 0과 73 사이의 숫자 중 3으로 끝나는 숫자만 출력되게 만드세요.

# 3 13 23 33 43 53 63 73

# for i in range(74):
#     if i%10 == 3:
#         print(i,end=' ')
#     else:None

# i = 0
# while True:
#     if i >=74:
#         break
                   
                   
              
#     if i%10 == 3:               
#         print(i, end=' ')
#     i += 1

# 18.6 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
# 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 1~200, 두 번째 입력 값의 범위는 10~200이며 
#  첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다).
# 다음 소스 코드를 완성하여 첫 번째 정수와 두 번째 정수 사이의 숫자 중 3으로 끝나지 않는 숫자가 출력되게 만드세요. 
# 정답에 코드를 작성할 때는 while True:에 맞춰서 들여쓰기를 해주세요.


# 입력
# 1 20
# 결과
# 1 2 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20

# start, stop = map(int, input().split())
 
# i = start
 
# while True:
#     if i<=stop:
#         if i%10 != 3:
#             print(i,end='')
#     i += 1

# while i <= stop:
#     if i % 10 != 3:
#         print(i, end=' ')
#     i += 1

# while True:
#     if i > stop:
#         break
#     elif i % 10 == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     i += 1

# for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
#     for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
#         print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
#     print('i:', i, '\n', sep='')

# for i in range(5):            # 5번 반복. 바깥쪽 루프는 세로 방향
#     for j in range(5):        # 5번 반복. 안쪽 루프는 가로 방향
#         print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
#                # (print는 출력 후 기본적으로 다음 줄로 넘어감)


# for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
#     for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
#         if j <= i:                # 세로 방향 변수 i만큼
#             print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print() 

# for i in range(5):
#     for j in range(5):
#         if i==j:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# 19.5 연습문제: 역삼각형 모양으로 별 출력하기
# 다음 소스 코드를 완성하여 역삼각형 모양으로 별이 출력되게 만드세요.

# for i in range(5):
#     for j in range(5):
#         if j>=i:
#             print('*',end='')                                                                   
#     print()

# 19.6 심사문제: 산 모양으로 별 출력하기

# 표준 입력으로 삼각형의 높이가 입력됩니다. 
# 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 이때 출력 결과는 예제와 정확히 일치해야 합니다. 
# 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.

# 3
# 결과
#   *
#  ***
# *****

# for i in range(num):
#     for j in range(1,i*2,2):
#         print("*".center(num*2))
#     print()
 
# # int(input())

# for i in range(1, num + 1):
#     print(" " * (num - i) + "*" * (2 * i - 1))


# 1에서 100까지 출력
# 3의 배수는 Fizz 출력
# 5의 배수는 Buzz 출력
# 3과 5의 공배수는 FizzBuzz 출력

# for i in range(1,101):
#     if i%15 == 0:
#         print('FizzBuzz',end=' ')
#     elif i%3 == 0:
#             print('Fizz',end= ' ')
#     elif i%5 == 0:
#         print('Buzz',end=' ')
#     else:
#         print(i, end = ' ')

print()

# for i in range(1, 101):              # 1부터 100까지 100번 반복
#     if i % 3 == 0 and i % 5 == 0:    # 3과 5의 공배수일 때
#         print('FizzBuzz',end=' ')            # FizzBuzz 출력
#     elif i % 3 == 0:                 # 3의 배수일 때
#         print('Fizz',end=' ')                # Fizz 출력
#     elif i % 5 == 0:                 # 5의 배수일 때
#         print('Buzz',end=' ')                # Buzz 출력
#     else:
#         print(i,end=' ')  

# for i in range(1,101):
#      print('Fizz'*(i%3 == 0) + 'Buzz'*(i%5 == 0) or i,end= ' ')


# 20.7 연습문제: 2과 11의 배수, 공배수 처리하기
# 다음 소스 코드를 완성하여 1부터 100까지의 숫자를 출력하면서 
# 2의 배수일 때는 'Fizz', 11의 배수일 때는 'Buzz', 2과 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요.

# for i in range(1,101):
#      print('Fizz'*(i%2 == 0 ) + "Buzz"*(i%11 == 0) or i,end= ' ')

# 20.8 심사문제: 5와 7의 배수, 공배수 처리하기
# 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 1~1000, 두 번째 입력 값의 범위는 10~1000이며 
#  첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 첫 번째 정수부터 두 번째 정수까지 숫자를 출력하면서 
# 5의 배수일 때는 'Fizz', 7의 배수일 때는 'Buzz', 5와 7의 공배수일 때는 'FizzBuzz'를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).

num = input().split()

for i in range(int(num[0]),int(num[1])+1):
    print('Fizz'*(i%5==0) + 'Buzz'*(i%7==0) or i)