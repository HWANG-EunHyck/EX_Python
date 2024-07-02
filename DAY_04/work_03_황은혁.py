# 12.4 연습문제: 딕셔너리에 게임 캐릭터 능력치 저장하기
# 다음 소스 코드를 완성하여 게임 캐릭터의 체력(health)과 이동 속도(movement speed)가 출력되게 만드세요.

camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health'],camille['movement_speed'])

# 표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다. 
# 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한 뒤 딕셔너리를 출력하는 프로그램을 만드세요. 
# input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.

# 입력
# health health_regen mana mana_regen
# 575.6 1.7 338.8 1.63
# 결과
# {'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}

key = input().split()
value = list(map(float,input().split()))
dict_1 = dict(zip((key),(value)))
print(dict_1)

# TODO FIXME BUG NOTE

x= 10 
if x ==10 :
    print('x= 10입니다')

x= 10 
if x ==10 :
    pass

x= 10
if x == 10:
    print('x는')
    print('10입니다')


x=15
if x >=10 :
    print('x는 10이상입니다')
    if x == 15:
        print('x는 15입니다')
    if x == 20:
        print('x는 20입니다')

x = int(input())

if x == 10:
    print('x는 10입니다')
if x == 20:
    print('x는 20입니다')

a = 1
if not a:
    print('False')

# 13.6 연습문제: if 조건문 사용하기
# 다음 소스 코드를 완성하여 x의 값이 10이 아닐 때 'ok'가 출력되게 만드세요.

x = 5
 
if x != 10 :                        
    print('ok')

# 13.7 심사문제: 온라인 할인 쿠폰 시스템 만들기
# 표준 입력으로 가격(정수)과 쿠폰 이름이 각 줄에 입력됩니다. 
# Cash3000 쿠폰은 3,000원, Cash5000 쿠폰은 5,000원을 할인합니다. 
# 쿠폰에 따라 할인된 가격을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).

# 입력
# 27000
# Cash3000
# 결과
# 24000

x= int(input())
y= input()
if y == 'Cash3000':
    print(x - 3000)
if y == 'Cash5000':
    print(x - 5000)
else:
    pass

x= 5
if x == 10:
    y=x
else:
    y=0

x= 5
y=x if x==10 else 8

print(y)


if True:
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')

if 0 :
    print('참')
else :
    print('거짓')
    
if 123145:
    print('참')
else :
    print('거짓')

if 'hi':
    print('참')
else:
    print('거짓')

if '':
    print('참')
else:
    print('거짓')

if not 0 :
    print('참')

else:
    print('거짓')

x = 10
y = 20

if x == 10 and y == 20:
    print('참')
else:
    print('거짓')


# 14.6 연습문제: 합격 여부 판단하기
# A 기업의 입사 시험은 필기 시험 점수가 80점 이상이면서 코딩 시험을 통과해야 합격이라고 정했습니다
# (코딩 시험 통과 여부는 True, False로 구분). 
# 다음 소스 코드를 완성하여 '합격', '불합격'이 출력되게 만드세요.

written_test = 75
coding_test = True
 
if  written_test >= 80 and  coding_test == True  :
    print('합격')
else:
    print('불합격')

# 실행 결과
# 불합격

# 14.7 심사문제: 합격 여부 판단하기
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 
# 여기서 네 과목의 평균 점수가 80점 이상일 때 합격이라고 정했습니다. 
# 평균 점수에 따라 '합격', '불합격'을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 단, 점수는 0점부터 100점까지만 입력받을 수 있으며 범위를 벗어났다면 '잘못된 점수'를 출력하고 합격,
# 불합격 여부는 출력하지 않아야 합니다.

# 89 72 93 82
# 결과
# 합격

x = list(map(int,input().split()))

if x[0]>100 or x[0]<0 or x[1]>100 or x[1]<0 or x[2]>100 or x[2]<0 or x[3]>100 or x[3]<0:
    print('잘못된 점수')    
elif sum(x)/len(x) >= 80:
    print('합격')
else:
    print('불합격')

x= 10

if x == 10:
    print('x=10')
elif x == 20:
    print('x=20')

# 15.3 연습문제: if, elif, else 모두 사용하기
# 다음 소스 코드를 완성하여 변수 x가 11과 20 사이면 '11~20', 21과 30 사이면 '21~30',
# 아무것도 해당하지 않으면 '아무것도 해당하지 않음'이 출력되게 만드세요.

x = int(input())

if  11<=x<=20:
    print('11~20')
elif 21<=x<=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# 15.4 심사문제: 교통카드 시스템 만들기
# 표준 입력으로 나이(만 나이)가 입력됩니다(입력 값은 7 이상 입력됨).
# 교통카드 시스템에서 시내버스 요금은 다음과 같으며 각 나이에 맞게 요금을 차감한 뒤 잔액이 출력되게 만드세요(if, elif 사용). 
# 현재 교통카드에는 9,000원이 들어있습니다.

# 어린이(초등학생, 만 7세 이상 12세 이하): 650원
# 청소년(중∙고등학생, 만 13세 이상 18세 이하): 1,050원
# 어른(일반, 만 19세 이상): 1,250원

# 17
# 결과
# 7950

age = int(input())
balance = 9000    # 교통카드 잔액

if 7<= age <=12:
    balance -= 650
elif 13<= age <= 18:
    balance -= 1050
else:
    balance -= 1250

print(balance)
