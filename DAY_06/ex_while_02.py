#-------------------------------------------------------------------
# 제어문 while 반복문
# ------------------------------------------------------------------
#[실습] 사용자로부터 데이터를 입력 받습니다. 사용자 'q' 또는 'Q'입력하기 전까지 입력을 받습니다.
data2 = []

while True:
    data = input()
    data2 += data
    if data == 'q' or data =='Q': break

print('end')

print(data2)