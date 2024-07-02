#---------------------------------
# 입력 & 출력 실습
#---------------------------------
# [실습1] 데이터 저장 및 변수 생성 그리고 출력
# - 생년월일
# - 띠
# - 혈액형
# - 출력형태 : 나는 0000년 00월 00일 0000띠입니다 
#             혈액형은 __ 0형입니다
#---------------------------------
birth = '20000101'
animal = '닭'
blood_type = 'O'

print(f'나는 {birth[:4]}년 {birth[4:6]}월 {birth[6:]}일 {animal}띠입니다 \n혈액형은 둥글둥글한 {blood_type}형입니다')
#---------------------------------
# [실습1] 입력 받은 데이터 저장 단, file로 저장
# - 좋아하는 계절 
# - 좋아하는 나라
# - 여행하고 싶은 나라
#---------------------------------

season = input('좋아하는 계절 : ')
Favorite_country = input('좋아하는 나라 : ')
walking_country = input('여행하고 싶은 나라 : ')

FILENAME = 'my_info.txt'

f = open(FILENAME, mode='w', encoding='utf-8')
print(season,Favorite_country,walking_country,sep = '\n' ,file = f)
# f.write(season)
# f.write('\n')
# print(f'좋아하는 계절 : {season}',file=f)
# print(f'여행하고 싶은 나라 : {walking_country}',file=f,end='')
f.close()

