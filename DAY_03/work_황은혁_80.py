# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.

print('Hello World')
print()
# 002 print 기초
# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)

print('Mary\'s cosmetics')
print()

# 003 print 기초
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
# 신씨가 소리질렀다. "도둑이야".
print("신씨가 소리질렀다. \"도둑이야\".")
print()

# 004 print 기초
# 화면에 C:\Windows를 출력하세요.
print('C:\\Windows')
print()

# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t\t반갑습니다.")
# => \n 은 줄바꿈 \t는 탭키만큼 칸 띄우기
print()

# 006 print 여러 데이터 출력
# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print ("오늘은", "일요일")
# 오늘은 일요일
print()

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print('naver','kakao','sk','samsung',sep = ';')
print()

# 008 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.

# naver/kakao/sk/samsung
print('naver','kakao','sk','samsung',sep = '\\')
print()

# 009 print 줄바꿈
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 
# 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.

# print("first");print("second")
print("first",end = '');print("second")
print()

# 010 연산 결과 출력
# 5/3의 결과를 화면에 출력하세요.
print(5/3)
print()

# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsung_cost = 50000
평가금액 = samsung_cost * 10
print(f'삼성 전자의 평가금액 : {평가금액} ')
print()

# 012 변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79

# 013 문자열 출력
s = "hello"
t = "python"

# 실행 예:
# hello! python

print(s+'!',t)
print()

# 014 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보세요.

# >> 2 + 2 * 3 

# 8

# 015 type 함수
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.

# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.

a = "132"
#=> ''로 씌워진 숫자이기 때문에 str
print(type(a))
print()

# 016 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환해보세요.

num_str = "720"

num_str = int(num_str)
print(num_str,type(num_str))
print()

# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.

num = 100
num = str(num)
print(num,type(num))
print()

# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

실수 = "15.79"
실수 = float(실수)
print(실수,type(실수))
print()

# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.

year = "2020"

year = int(year)

print(year,year+1,year+2)
print()

# 020 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
# 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

month_pay = 48584
need_month = 36
print(f'총금액 : {month_pay * need_month}')
print()

# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.

letters = 'python'
# 실행 예
# p t
print(letters[0],letters[letters.find('t')])
print(letters[0:3:2])
print()
# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.

license_plate = "24가 2210"
# 실행 예: 2210

print(license_plate[4:])
print()

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.

string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

print(string[::2])
print()
# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.

string = "PYTHON"
# 실행 예:
# NOHTYP

print(string[::-1])
print()
# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.

phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222

print(phone_number[:3],phone_number[4:8],phone_number[9:])
print(phone_number.replace('-',' '))
print()
# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.

# 실행 예
# 01011112222
print(phone_number.replace('-',''))
print()

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.

url = "http://sharebook.kr"
# 실행 예:
# kr

print(url[url.find('.')+1:])
print()
# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.

lang = 'python'
# lang[0] = 'P'
print(lang)
#==> Python이 출력 인줄 알았는데 str은 tuple range와 마찬가지로 고쳐쓰기가 불가함
print()

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A

print(string.replace('a','A'))
print()

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.

string = 'abcd'
string.replace('b', 'B')
print(string)
# ==> 따로 객체 지정을 해주지 않아서 그냥 abcd가 나옴
print()

# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.

a = "3"
b = "4"
print(a + b)
#==>str 34
print()

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.

print("Hi" * 3)
#==> HiHiHi
print()

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.

# 실행 예:
# --------------------------------------------------------------------------------

print('-'*80)
print()

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.

t1 = 'python'
t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.

# 실행 예:
# python java python java python java python java

print((t1+' '+t2+' ')*4)
print()
# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

print('이름: %s 나이: %s'%(name1,age1))
print('이름: %s 나이: %s'%(name2,age2))
print()

# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.

상장주식수 = "5,969,782,550"

상장주식수 = 상장주식수.replace(',','')
print(상장주식수,type(상장주식수))
상장주식수_int = int(상장주식수)
print(상장주식수_int,type(상장주식수_int))
print()
# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.

분기 = "2020/03(E) (IFRS연결)"

print(분기[:분기.find('(')])
print()
# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.

data = "   삼성전자    "

print(data.strip())
print()
# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.

ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)
print()
# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.

ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)
print()
# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.

msg = 'hello'
msg = msg.capitalize()
print(msg)
print()
# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.

a = "hello world"
b = a.split(' ')
print(b)
print()
# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.

ticker = "btc_krw"
ticker = ticker.split('_')
print(ticker)
print()
# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.

date = "2020-05-01"
date = date.split('-')
print(date)
print()
# 051 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 
# 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)

movie_rank = ['닥터 스트레인지', '럭키','스플릿']
print(movie_rank,type(movie_rank))
print()
# 052 리스트에 원소 추가
# 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append('배트맨')
print(movie_rank,type(movie_rank))
print()
# 053
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
# "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

movie_rank.insert(1,'슈퍼맨')
print(movie_rank,type(movie_rank))
print()
# 054
# movie_rank 리스트에서 '럭키'를 삭제하라.

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

del movie_rank[3]
print(movie_rank,type(movie_rank))
print()

# 055
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

del movie_rank[2:]
print(movie_rank,type(movie_rank))
print()

# 056
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
# 실행 예:
# >> langs
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

lang = lang1 + lang2
print(lang)
print()

# 057
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)

nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예:
max:  7
min:  1

max = max(nums);min = min(nums)
print(f'max: {max}\nmin: {min}')
print()

# 058
# 다음 리스트의 합을 출력하라.

nums = [1, 2, 3, 4, 5]
# 실행 예:
# 15

합 = sum(nums)
print(합)
print()

# 059
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(f'리스트에 저장된 데이터의 개수 : {len(cook)}')
print()

# 다음 리스트의 평균을 출력하라.

nums = [1, 2, 3, 4, 5]
# 실행 예:
# 3.0

print(f'리스트의 평균을 구하라 : {sum(nums)/len(nums)}')
print()
# 061
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)

price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]

print(price[1:])
print()
# 062
# 슬라이싱을 사용해서 홀수만 출력하라.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]

print(nums[::2])
print()
# 063
# 슬라이싱을 사용해서 짝수만 출력하라.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]

print(nums[1::2])
print()
# 064
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.

nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]

print(nums[::-1])
print()
# 065
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자 Naver

print(interest[0],interest[2])
print()
# 067 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

print('/'.join(interest))
print()

# 068 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우

print('\n'.join(interest))
print()

# 069 문자열 split 메서드
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.

string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.

# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

interest = string.split('/')
print(interest)
print()
# 070 리스트 정렬
# 리스트에 있는 값을 오름차순으로 정렬하세요.

data = [2, 4, 3, 1, 5, 10, 9]
data1 = sorted(data)
print(data1)
print()

# 071
# my_variable 이름의 비어있는 튜플을 만들라.

my_variable =()
my_variable1 = tuple()

print(my_variable,type(my_variable))
print(my_variable1,type(my_variable1))
print()

# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 
# 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)

movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print()
# 073
# 숫자 1 이 저장된 튜플을 생성하라.

one = 1,
print(one,type(one))
print()

# 074
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.

t = (1, 2, 3)
#  t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# ==> 튜플은 원소/요소의 변경이 되지 않습니다

# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?

t = 1, 2, 3, 4
# ==> 튜플입니다 
print(t,type(t))
print()

# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.

t = ('a', 'b', 'c')

t = ('A', 'b', 'c')
print()

# 077
# 다음 튜플을 리스트로 변환하라.

interest = ('삼성전자', 'LG전자', 'SK Hynix')

interest1 = list(interest)
print(interest1,type(interest1))
print()

# 078
# 다음 리스트를 튜플로 변경하라.

interest = ['삼성전자', 'LG전자', 'SK Hynix']

interest1 = tuple(interest)
print(interest1,type(interest1))
print()

# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# a,b,c가 각각 apple banana cake 의 주소를 할당받아서 출력결과는 apple banana cake

# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.

# (2, 4, 6, 8 ... 98)

tuple_짝 = tuple(range(2,99,2))
print(tuple_짝,type(tuple_짝))
print()