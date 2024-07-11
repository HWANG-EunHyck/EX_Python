## 모듈 내에서 일부 변수, 함수 ,클래스만 포함하는 경우
## - 형식 : from 모듈명 import 변수명/함수명/클래스명
## - 주의 : 파일안에 동일한 변수명/함수명/클래스가 존재한다면 해당파일에 변수명/함수명/클래스 사용됨~!
from math import pi,factorial,e
from random import *       # * 의미 : 모든 것 
from my_func import *

## 전역변수 ----------------------------------------
## 이름이 같다면  파일안에 있는 것을 우선시한다 
# pi ="Apple"

## 사용 : 바로 변수명/함수()/클래스명
print(f'내장모듈 math안에 있는 pi변수사용 : {pi}')
print(f'내장모듈 math안에 있는 pi변수사용 : {e}')
# 사용하지 않으면 회색으로 출력
# print(factorial(5))

print(random(),randint(2,6))

print(add(1,5))