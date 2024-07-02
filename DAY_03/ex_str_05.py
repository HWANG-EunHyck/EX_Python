#----------------------------
# 문자열 str 데이터 다루기
# - 이스케이프문자 : 특수한 의미를 가지는 문자
#   * 형식 : \문자1개
#   * '\n' - 줄 바꿈 문자
#   * '\t' - 탭 간격 문자
#   * '\'' - 홑따옴표 문자
#   * '\"' - 쌍따옴표 문자
#   * '\\' - \ 백슬러시 문자, 경로(path),URL관련

#   * '\U' - 유니코드 
#   * '\A' - 알람
#----------------------------
msg = '오늘은 좋은날\n내일은 주말이라 행복해'
print(msg)

msg = "오늘은 나의 \'생일\'이야"
print(msg)

# file = 'C:\Users\a\Saved Games\text.txt'
file = 'C:\\Users\\a\\Saved Games\\text.txt'
print(file)

# r' ' 또는 R' ': 문자열 내 이스케이프 문자는 무시됨
file = r'C:\Users\a\Saved Games\text.txt'
print(file)

msg1 = 'Happy\tNew\tyear'
msg2 = R'Happy\tNew\tyear'
print(msg1,msg2,sep =' => ')