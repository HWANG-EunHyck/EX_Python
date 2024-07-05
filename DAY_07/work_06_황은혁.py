# a = [10, 20, 30]

# a.append(100)

# print(a)

# a.extend([100,200,300])

# print(a)

# a.insert(-1,250)

# print(a)

# a.insert(9,400)

# print(a)

# a[1] = 21

# print(a)

# a[1:1] = [17,19]

# print(a)

# print(a.index(17))

# print(a.count(21))

# b = sorted(a)

# print(b)

# c = a.copy()

# print(c)

# a = [12,656,1,45,77]
# small = a[0]

# for i in a:
#     if i>small:
#         small = i
# print(small)

# a= [i for i in range(10)]
# print(a)

# b = [i+5 for i in range(10)]
# print(a)

# c= list(i*2 for i in range(10))
# print(c)

# a=[i for i in range(10) if i%2 ==0]
# print(a)

# a=[i+5 for i in range(10) if i%2 ==0]
# print(a)

# b = [i*n for i in range(2,10) for n in range(1,10)]
# print(b)

# a,b = list(map(int,input().split()))

# print(a,b)

# a = tuple(i for i in range(10) if i%2==0)
# # <generator object <genexpr> at 0x000002A247E2BDD0>
# print(a)

# 22.9 연습문제: 리스트에서 특정 요소만 뽑아내기
# 다음 소스 코드를 완성하여 리스트 a에 들어있는 
# 문자열 중에서 길이가 5인 것들만 리스트 형태로 출력되게 만드세요(리스트 표현식 사용).

# # practice_list_comprehension.py
# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
# b = [i for i in a if len(i)>5 ]
 
# print(b)

# 22.10 심사문제: 2의 거듭제곱 리스트 생성하기
# 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 1~20, 
#  두 번째 입력 값의 범위는 10~30이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요.
# 출력 결과는 리스트 형태라야 합니다.

# 예
# 입력
# 1 10
# 결과
# [2, 8, 16, 32, 64, 128, 256, 1024]

# a,b = list(map(int,input().split()))

# c = [2**i for i in range(a,b+1)]
# del c[1],c[-2]
# print(c)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.setdefault('e')
# x.setdefault('f',60)

# print(x)

# x.update(e= 50)

# print(x)

# x.update(a=1,b=2,c=3,d=4,e=5)
# print(x)

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
