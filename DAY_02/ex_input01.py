#---------------------------------
#   내장함수 input() 사용법
# - 키보드로부터 입력한 데이터를 받아오는 내장함수
# - 문법 : input('요청 문자열')
# - 특징 : 입력 후 Enter키 입력이 되어야지만 데이터 전달됨
#          즉, 입력이 완료될떄까지 멈춤
#---------------------------------
# 이름 입력 받기

name = input('이름을 입력하세요: ')
print(f'내 이름은 {name}입니다')