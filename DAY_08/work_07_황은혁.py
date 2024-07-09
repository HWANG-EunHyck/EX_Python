# keys = ['a', 'b', 'c', 'd']
# x = dict.fromkeys(keys)
# print(x)

# y = dict.fromkeys(keys,100)
# print(y)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key, value in x.items():
#     print(key, value)

# keys = ['a', 'b', 'c', 'd']

# # x = {key : value for key,value in dict.fromkeys(keys).items()}

# # print(x)
# y = dict.fromkeys(keys)
# print(y)

# x ={i:0 for i in dict.fromkeys(keys,100).keys()}

# x= {i:0 for i in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}

# print(x)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x= {key:value for key,value in x.items() if value !=20}

# print(x)

# x.pop('a','b')
# print(x)

# terrestrial_planet = {
#     'Earth': {
#         'physical_characteristics': {
#             'mean_radius': 6371.0,
#             'mass': 5.97219E+24
#         },
#         'orbital_characteristics': {
#             'orbital_period': 365.25641,
#             'satellites': 1
#         }


# 25.7 연습문제: 평균 점수 구하기
# 다음 소스 코드를 완성하여 평균 점수가 출력되게 만드세요.

# practice_dict_average.py
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
# # sum = 0
# # for i in maria.values():
# #     sum += i
# # average = sum /len(maria)
# average = sum(maria.values())/len(maria)
                                          
# print(average)
# 실행 결과
# 89.25

# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고, 
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다. 
# 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.

# 예
# 입력
# alpha bravo charlie delta
# 10 20 30 40
# 결과
# {'alpha': 10, 'bravo': 20}

# judge_dict_del.py
# keys = input().split()
# values = map(int, input().split())
 
# x = dict(zip([keys], [values]))
 
# del x['delta'] 
# x = {i:j for i,j in x.items() if j != 30}

# print(x)

# 23.6 연습문제: 3차원 리스트 만들기
# 다음 소스 코드를 완성하여 높이 2, 세로 크기 4, 가로 크기 3인 3차원 리스트를 만드세요(리스트 표현식 사용).

# practice_three_dimensional_list.py

# 실행 결과
# [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

# a = [ [[0*i for i in range(3)] for j in range(4)] for i in range(2)    ]
 
# print(a)

# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 
# 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다. 
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다. 
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).

# 여러 줄을 입력 받으려면 
# 다음과 같이 for 반복문에서 input을 호출한 뒤 append로 각 줄을 추가하면 됩니다
#     (list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).

# matrix = []
# for i in range(row):
#     matrix.append(list(input()))
# 이 문제는 지금까지 심사문제 중에서 가장 어렵습니다. 
# 처음 풀어보는 경우 대략 두 시간은 걸립니다. 시간을 두고 천천히 고민해서 풀어보세요. 
# 지금까지 학습한 내용을 모두 동원해야 풀 수 있으며 
# 막힐 때는 지금까지 학습한 내용을 다시 복습하면서 힌트를 찾아보세요.

# 예
# 입력
# 3 3
# .**
# *..
# .*.
# 결과
# 2**
# *43
# 2*1

# col,row = list(map(int,input().split()))

# for i in range(row):
#     matrix.append(list(input()))


# [['.', '*', '*'], ['*', '.', '.'], ['.', '*', '.']]
# 가로 세로
# col = 3
# row = 3

# matrix = [['.', '*', '*'], ['*', '.', '.'], ['.', '*', '.']]

# for i in matrix:
#     for j in i:
#         cnt = 0
#         if j =:
#             j = 
#             print(j,end ='')
#         elif j == '*':
#             print("*",end='')
#     print()


# table = str.maketrans('aeiou', '12345')
# print('apple'.translate(table))

# 24.4 연습문제: 파일 경로에서 파일명만 가져오기
# 다음 소스 코드를 완성하여 파일 경로에서 파일명만 출력되게 만드세요.
# 단, 경로에서 폴더의 깊이가 달라지더라도 파일명만 출력할 수 있어야 합니다.

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
                                      
filename = path[path.rfind('\\')+1:]
                                      
 
print(filename)
# 실행 결과
# python.exe

# 24.5 심사문제: 특정 단어 개수 세기

# 표준 입력으로 문자열이 입력됩니다. 
# 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야 합니다.



# 예
# 입력
# #the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.
# 결과
# 6

# data = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
# data = input()
# data = data.replace("'",'')
# data = data.replace(".",'')
# data = data.replace(",",'')
# data = data.replace('-',' ')
# data = data.split()
# print(data.count('the'))


# 24.6 심사문제: 높은 가격순으로 출력하기
# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 
# 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 
# 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.

# 51900;83000;158000;367500;250000;59200;128500;1304000
# 결과
# 1,304,000
#   367,500
#   250,000
#   158,000
#   128,500
#    83,000
#    59,200
#    51,900

# data = list(map(int,input().split(';')))
# data = sorted(data,reverse=True)
# data2= []
# for i in data:
#     data2.append(format(i, ','))
# for i in data2:
#     print('{:>9}'.format(i))

# 29.3 연습문제: 몫과 나머지를 구하는 함수 만들기
# 다음 소스 코드를 완성하여 x를 y로 나누었을 때의 몫과 나머지가 출력되게 만드세요

# x = 10
# y = 3
 
# def get_quotient_remainder(x,y):
#     return x//y,x%y

# quotient, remainder = get_quotient_remainder(x, y)
# print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

# 실행 결과
# 몫: 3, 나머지: 1

# 표준 입력으로 숫자 두 개가 입력됩니다. 
# 다음 소스 코드를 완성하여 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 출력되게 만드세요. 
# 이때 나눗셈의 결과는 실수라야 합니다.


# x, y = map(int, input().split())
# def calc(x,y):
#     return x+y,x-y,x*y,x/y

# a, s, m, d = calc(x, y)
# print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
# 예
# 입력
# 10 20
# 결과
# 덧셈: 30, 뺄셈: -10, 곱셈: 200, 나눗셈: 0.5


# korean, english, mathematics, science = 100, 86, 81, 91
 
# def get_max_score(*args):
#     return max(args)           
 
# max_score = get_max_score(korean, english, mathematics, science)
# print('높은 점수:', max_score)
 
# max_score = get_max_score(english, science)
# print('높은 점수:', max_score)
# # 실행 결과
# 높은 점수: 100
# 높은 점수: 91

# 30.7 심사문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 
# 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가 출력되게 만드세요. 
# 평균 점수는 실수로 출력되어야 합니다.

# 76 82 89 84
# 결과
# 낮은 점수: 76.00, 높은 점수: 89.00, 평균 점수: 82.75
# 낮은 점수: 82.00, 높은 점수: 84.00, 평균 점수: 83.00

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
        return min(args),max(args)

def get_average(**kwargs):
    total = sum(kwargs.values())
    cnt = len(kwargs)
    return total / cnt

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
# 예
# 입력
# 76 82 89 84
# 결과
# 낮은 점수: 76.00, 높은 점수: 89.00, 평균 점수: 82.75
# 낮은 점수: 82.00, 높은 점수: 84.00, 평균 점수: 83.00