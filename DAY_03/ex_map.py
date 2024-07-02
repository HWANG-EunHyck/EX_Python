#----------------------------
# 내장함수 map(함수명,여러개데이터)
#----------------------------
data =input('숫자 데이터 입력 : ').split()

print(data)
print(type(data),type(data[0]))

data = map(int,data)
data1 = list(map(int,data))

print()
print(type(data))
print(data)

print()
print(type(data1))
print(data1)