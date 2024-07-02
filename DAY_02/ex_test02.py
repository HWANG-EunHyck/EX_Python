#---------------------------------
# 연산자 실습
#---------------------------------
# [실습] 문자열 데이터 2개에 대한 논리 연산 수행 후 출력
data1 = 'Hello' 
data2 = 'hello'

print(f'{data1} > {data2} ==> {data1>data2}')
print(f'{data1} < {data2} ==> {data1<data2}')
print(f'{data1} == {data2} ==> {data1==data2}')
print(f'{data1} != {data2} ==> {data1!=data2}')


#---------------------------------
# [실습] 정수 1개와 문자열 1개에 대한 논리 연산 수행 후 출력
#        단, not 연산자만 사용
num1 = 3.2 
# num1 = 0 
# msg = '원더우먼'
msg = ''

print(f'not {num1}  ==> {not num1} ')
print(f'not {msg} ==> {not msg}')
