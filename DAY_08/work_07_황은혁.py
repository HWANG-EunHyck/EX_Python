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

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x= {key:value for key,value in x.items() if value !=20}

print(x)

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
keys = input().split()
values = map(int, input().split())
 
x = dict(zip([keys], [values]))
 
del x['delta'] 
x = {i:j for i,j in x.items() if j != 30}

print(x)

