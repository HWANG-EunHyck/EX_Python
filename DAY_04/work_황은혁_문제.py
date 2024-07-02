# 081 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다.
# 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.

# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, 
# start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score,a,b = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

print(valid_score)
print()
# 082
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, 
# start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

a,b,*valid_score = scores

print(valid_score)
print()
# 083
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때,
# start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

a,*valid_score,b = scores

print(valid_score)
print()
# 084 비어있는 딕셔너리
# temp 이름의 비어있는 딕셔너리를 만들라.

temp= {}

print(type(temp))
print()
# 085
# 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.

price = dict(zip(['메로나','폴라포','빵빠레'],[1000,1200,1800]))


print(price)
print()
# 086
# 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.

price['죠스바'] = 1200
price['월드콘'] = 1500

print(price)
print()
# 087
# 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
print(f"메로나 가격 : {price['메로나']}")
print()

# 088
# 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
price['메로나'] = 1300
print(price)
print()

# 089
# 다음 딕셔너리에서 메로나를 삭제하라.

del price['메로나']
print(price)
print()

# 090
# 다음 코드에서 에러가 발생한 원인을 설명하라.
# ==> 없는 키값을 줘서 에러 발생

# 091 딕셔너리 생성
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라.
# 딕셔너리의 이름은 inventory로 한다.

inventory = dict(zip(['메로나','비비빅','죠스바'],[[300,20],[400,3],[250,100]]))

print(inventory,type(inventory))
print()
# 092 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.

print(inventory['메로나'][0],'원')
print()
# 093 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print(inventory['메로나'][1],'개')
print()
# 094 딕셔너리 추가
# inventory 딕셔너리에 아래 데이터를 추가하라.
inventory['월드콘'] = [500,7]
print(inventory)
print()
# 095 딕셔너리 keys() 메서드
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

icecream_keys = list(icecream.keys())
print(list(icecream.keys()))
print()
# 096 딕셔너리 values() 메서드
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

icecream_values = list(icecream.values())
print(icecream_values)
print()

# 097 딕셔너리 values() 메서드
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
총합 = sum(icecream_values)
print(총합)
print()
# 098 딕셔너리 update 메서드
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream['팥빙수'] = 2700
icecream['아맛나'] = 1000

# icecream.update(new_product)

print(icecream)
print()
# 099 zip과 dict
# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

result = dict(zip((keys),(vals)))
print(result)
print()
# 100 zip과 dict
# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price))
print(close_table)
print()

# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?

## ==> bool 타입

#  102
# 아래 코드의 출력 결과를 예상하라

print(3 == 5)
# False
print()

# 103
# 아래 코드의 출력 결과를 예상하라

print(3 < 5)
# True

print()

# 104
# 아래 코드의 결과를 예상하라.

x = 4
print(1 < x < 5)
#True
print()

# 105
# 아래 코드의 결과를 예상하라.

print ((3 == 3) and (4 != 3))
# True
print()

# 106
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.

# print(3 => 4)
# '=>' 이게 아니라 '>='다

# 107
# 아래 코드의 출력 결과를 예상하라

if 4 < 3:
    print("Hello World")
# if의 결과 값이 False 이므로 아무일도 일어나지 않는다 

# 108
# 아래 코드의 출력 결과를 예상하라

if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

# if의 조건값이 False 이므로 넘어가서 else 부분을 실행하여 'Hi,there.'가 출력된다.

# 109
# 아래 코드의 출력 결과를 예상하라

if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1\n2\n4
print()
# 110
# 아래 코드의 출력 결과를 예상하라

if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 3\n5
print()
# 111
# 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.

# >> 안녕하세요
# 안녕하세요안녕하세요

# msg = input()
msg = '안녕하세요'
print(msg*2)
print()

# 112
# 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.

# >> 숫자를 입력하세요: 30
# 40

# num = int(input('숫자를 입력하세요: '))
num = 30
print(num+10)
print()
# 113
# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.

# >> 30
# 짝수

# num = int(input())
num= 30
if num%2==0:
    print('짝수')
else:
    print('홀수')

print()
# 114
# 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.

# >> 입력값: 200
# 출력값: 220
# >> 입력값: 240
# 출력값: 255

# num = int(input('입력값: '))
num = 200
if num + 20 >225:
    print('출력값: 225')
else:
    print(f'출력값: {num + 20}')

print()

# 115
# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 
# 단 출력 값의 범위는 0~255이다. 
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.

# >> 입력값: 200
# 출력값: 180
# >> 입력값: 15
# 출력값: 0

# num = int(input('입력값: '))
num = 200
num -= 20

if 0<=num<=255:
    print(f'출력값: {num}')
elif num<0:
    print('출력값: 0')
else:
    print('출력값: 255')

print()
# 116
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.

# >> 현재시간:02:00
# 정각 입니다.
# >> 현재시간:03:10
# 정각이 아닙니다

# time = input('현재시간:').split(':')
time = [20,00]

if time[1] == '00':
    print('정각 입니다.')
else:
    print('정각이 아닙니다')

print()

# 117
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

fruit = ["사과", "포도", "홍시"]
# >> 좋아하는 과일은? 사과
# 정답입니다.

# 과일 = input('좋아하는 과일은? ')
과일 = '사과'

if  과일 in fruit:
    print('정답입니다')
else:
    print('오답입니다')

print()

# 118
# 투자 경고 종목 리스트가 있을 때 
# 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# 종목 = input('종목을 입력하시오: ')
종목 = 'Microsoft'
if 종목 in warn_investment_list:
    print('투자 경고 종목입니다')
else:
    print('투자 경고 종목이 아닙니다')
print()

# 119
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 제가좋아하는계절은: 봄
# 정답입니다.

# season = input('제가좋아하는계절은: ')
season = '봄'
if season in fruit.keys():
    print('정답입니다')
else:
    print('오답입니다')
print()
# 120
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 
# 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 좋아하는과일은? 한라봉
# 오답입니다.

# 과일 = input('좋아하는과일은?: ')
과일 = '한라봉'
if 과일 in fruit.values():
    print('정답입니다')
else:
    print('오답입니다')

print()

# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.

# >> a
# A

# string = input()
string = 'a'
if string.isupper():
    print(string.lower())
else:
    print(string.upper())
print()
# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.

# score = int(input())
score = 99
if 81<= score <=100:
    print('grade is A') 
elif 61 <=score <= 80:
    print('grade is B')
elif 41 <=score <= 60:
    print('grade is C')
elif 21 <=score <= 40:
    print('grade is D')
else:
    print('grade is E')

print()

# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 
# 각 통화별 환율은 다음과 같다. 
# 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다

# money = input().split(' ')
money = [100, '달러']
# if money[1] == '달러':
#     print(f'{float(1167 * int(money[0]))} 원')
# elif money[1] == '엔':
#     print(f'{1.096 * int(money[0])}')
# elif money[1] == '엔':
#     print(f'{1268 * int(money[0])}')
# else:
#     print(f'{171 * int(money[0])}')

dict = {'달러' : 1167 , "엔": 1.096, "유로": 1268, "위안": 171}

print(float(money[0])*dict[money[1]])
print()
# 124
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20

list=[]

# num1 = int(input('number1:'))
# num2 = int(input('number2:'))
# num3 = int(input('number3:'))
num1,num2,num3 = [10,9,20]

list.append(num1)
list.append(num2)
list.append(num3)

print(max(list))
print()
# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 
# 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.

# 통신사 = { '011' : 'SKT', '016':'KT', '019':'LGU','010':'알수없음'}

# p_num = input('휴대전화 번호 입력 : ').split('-')
p_num = ['010','222','2222']
if p_num[0] == '011':
    print('당신은 SKT 사용자입니다')
elif p_num[0] == '016':
    print('당신은 KT 사용자입니다')
elif p_num[0] == '019':
    print('당신은 LGU 사용자입니다')
else:
    print('알수없음')

print()

# 126
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다.
#  예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.

# -	0	1	2	3	4	5	6	7	8	9
# 01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라

# >> 우편번호: 01400
# 도봉구

juso = input('우편번호 : ')

if juso[:3] in ['010','011','012']:
    print('강북구')
elif juso[:3] in ['013','014','015']:
    print('도봉구')
else:
    print('노원구')

print()

# 127
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

# >> 주민등록번호: 821010-1635210
# 남자

jumin = input('주민번호를 입력하세요 : ')
jumin = jumin.split('-')[1]


if jumin[0] in ['1','3'] : 
    print('남자')
else :
    print('여자')

# 128
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라

# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
# >> 주민등록번호: 821010-1635210
# 서울이 아닙니다.
# >> 주민등록번호: 861010-1015210
# 서울 입니다.

jumin = input('주민번호를 입력하세요 : ')
jumin = jumin.split('-')[1]

if 0<= int(jumin[1:3]) <= 8 : 
    print('서울 입니다.')
else :
    print('서울이 아닙니다.')
print()

# 129
# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5 
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다.
# 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.

# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.

jumin = input('주민번호를 입력하세요 : ')
jumin = jumin.split('-')
jumin = list(jumin[0]) + list(jumin[1])
ok = (int(jumin[0]) * 2 ) + (int(jumin[1]) * 3 ) +(int(jumin[2]) * 4 ) +(int(jumin[3]) * 5 )+ (int(jumin[4]) * 6 )+(int(jumin[5]) * 7 ) +  (int(jumin[6]) * 8 ) + (int(jumin[7]) * 9 )+ (int(jumin[8]) * 2 ) + (int(jumin[9]) * 3 ) + (int(jumin[10]) * 4 ) + (int(jumin[11]) * 5 )
ok = 11- (ok % 11)

if jumin[-1] == str(ok):
    print('유효합니다')
else:
    print('유효하지않습니다')

print(jumin[-1],ok)

#130
#아래3 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.

#import requests
#btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 
#최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장",
#그렇지 않은 경우 "하락장" 문자열을 출력하라.

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

print(btc.keys())

gap = (float(btc['max_price']) - float(btc['min_price']))
up_down = float(btc['max_price']) -(float(btc['opening_price'])+ gap)

print(gap, up_down)

if up_down> 0 :
  print('상승장')
elif up_down<0:
  print('하락장')
else:
  print(0)