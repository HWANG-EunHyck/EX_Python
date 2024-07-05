# -------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드 살펴보기
# -------------------------------------------------
## [1개 문자열을 여러개 문자열로 분리해주는 메서드 split()]
## - 분리기준 -> 기본값 : 공백

msg = ' Happy New Year '

m1 = msg.split()

print(f'msg : {msg} ---- m1 : {m1}, {type(m1)}')

phone = "010-2222-3333"
presult=phone.split('-')
print(f'msg : {phone} ---- m1 : {presult}, {type(presult)}')

msg = "오늘은 날씨가 좋군요. 내일도 날씨가 좋을까요?"
result=msg.split('.')
print(f'msg : {msg} ---- m1 : {result}, {type(result)}')

## [여러개 문자열을 한개의 문자열로 만들어주는 메서드 join()]
## - 합칠문자.join(여러개 문자열)
## -> 010*1111*2222
con = ' * '
phone2 = con.join(presult)
print(f'msg : {presult} ---- m1 : {phone2}, {type(phone2)}')

## -> 010*1111*2222
con = '_'
phone2 = con.join(presult)
print(f'msg : {presult} ---- m1 : {phone2}, {type(phone2)}')

## -> 010*1111*2222
con = '/'
phone2 = con.join(presult)
print(f'msg : {presult} ---- m1 : {phone2}, {type(phone2)}')
