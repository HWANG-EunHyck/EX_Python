#----------------------------
# 내장함수 
#----------------------------
# 숫자 데이터 절대값 계산해주는 내장함수 abs(n)

print(abs(-9))

# 최대값,최솟삾 찾아주는 내장함수 max(),min()
print(max(10,2,31),min(10,2,31))

a = 1,2,3,4,5
print(max(a))

# 제곱근 계산 내장함수 pow()
print('연산자 ** : ', 2**4)
print('pow() : ' , pow(2,4) )

# 파일관련 내장함수 open(파일명, 동작모드,인코딩)
# - 기본값 : 동작모드 - 읽기 read
#            인코딩 - 시스템 따라서

FILENAME = 're.txt'

#(1) 파일 열기 - 쓰기 모드
f = open(FILENAME,mode = 'w',encoding='utf-8')

#(2) 데이터 쓰기
f.write('호호호')
f.write('\n')
print(f'호호호' ,file =f)

#(3) 파일닫기
f.close()
