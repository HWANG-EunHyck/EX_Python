#----------------------------
# 문자열 str 데이터 다루기
# - 문자요소 연산 : 산술 ,비교, 멤버 연산
#----------------------------
# [1] 산술 연산
data1 = 'Happy'
data2 = "Year"

#뎃셈(+)연산 : str+str => str연결
print(data1 + data2)
# print(data1 + 10) 문자열 + 숫자는 허용하지 않는다
print(data1 + '10')
print(data1 + str(10))

#뺄셈(-)연산 : str-str => str연결 : 미지원
# print(data1 - data2)

#곱셈(*)연산 : str*int => 숫자만큼 str 연결
print(data1 * 9)

#----------------------------
# [1] 멤버 연산
# - 요소/ 원소 in 문자열     ==> 존재하면 True , 아니면 False
# - 요소/ 원소 not in 문자열 ==> 존재 X  True, 아니면 False

print(f'H in {data1} : {"H" in data1}')

# print(3 in 123)