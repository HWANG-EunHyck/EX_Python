# -------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드 살펴보기
# -------------------------------------------------
msg = "Hello 0705!"
#      01234567890
# [원소 요소 인덱스 찾기 메서드 - find(문자 1개 또는 문자열)]
# - 'H'의 인덱스
idx_H = msg.find('H')
print(f'H의 인덱스 : {idx_H}')

idx_7 = msg.find('7')
print(f'H의 인덱스 : {idx_7}')

idx_llo = msg.find('llo')
print(f'H의 인덱스 : {idx_llo}')

# 대소문자 일치, 존재하지 않으면 -1을 반환
idx_llO = msg.find('llO') 
print(f'H의 인덱스 : {idx_llO}')
print()
# [원소 요소 인덱스 찾기 메서드 - index(문자 1개 또는 문자열)]

idx_H = msg.index('H')
print(f'H의 인덱스 : {idx_H}')

idx_llo = msg.index('llo')
print(f'H의 인덱스 : {idx_llo}')

# value ERROR => 존재하지 않으면 ERROR 발생
if "llO" in msg:
    idx_llO = msg.index('llO')
    print(f'H의 인덱스 : {idx_llO}')
print('없습니다')
print()

# -------------------------------------------------
# 문자열에 동일한 문자가 여러개 존재하는 경우
# -------------------------------------------------
# 전에껄 업데이트 해서 사용
# idx => idx+1 => idx+2 => idx+3
msg = "Good Luck Good"

# - 'o'의 인덱스 찾기 => 첫번쨰 'o' 인덱스

# idx_o_1 = msg.find('o')
# print(f'o의 첫번째 인덱스 : {idx_o_1}')

# # - 'o'의 인덱스 찾기 => 두번쨰 'o' 인덱스

# idx_o_2 = msg.find('o',idx_o_1+1)
# print(f'o의 두번째 인덱스 : {idx_o_2}')

# # - 'o'의 인덱스 찾기 => 세번쨰 'o' 인덱스

# idx_o_3 = msg.find('o',idx_o_2+1)
# print(f'o의 세번째 인덱스 : {idx_o_3}')

# # - 'o'의 인덱스 찾기 => 네번쨰 'o' 인덱스

# idx_o_4 = msg.find('o',idx_o_3+1)
# print(f'o의 세번째 인덱스 : {idx_o_4}')
idx = -1
for i in range(msg.count('o')):
    idx = msg.find('o',idx+1)
    print(f'{i+1}번째 o 의 인덱스 : {idx}')
print()
# -------------------------------------------------
# 문자열의 뒷부분부터 찾는 메서드 ==> rfind(),rindex()
# 문자 시작인덱스 끝인덱스+1
# -------------------------------------------------

msg = "Happy year yyyy"

# - 첫번째 'y' 인덱스 찾기
idx = msg.rfind('y')
print(idx)

# - 두번쨰 'p' 인덱스 찾기
idx = msg.rfind('y',0,idx)
print(idx)
print()

# - 파일명에서 확장자 txt,jpeg,gz 찾기
files = ['hello.txt', '2024상반지경제분석.doc','kakao_123456789.jpg']

for i in files:
    print(i.split('.')[1])

for i in files:
    print(i[i.find('.')+1:])


