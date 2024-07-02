#----------------------------
# tuple 데이터 자료형 살펴보기
# - 내장함수 : len(), max(), min(), sum()
# - 연산자 : 덧셈, 곱셈, 멤버연산자
#----------------------------
nums = 11,22,33,44,55,1

# 내장함수 ---------------------
print(f'nums의 개수 :{len(nums)}')
print(f'nums의 최대값 :{max(nums)}')
print(f'nums의 최솟값 :{min(nums)}')
print(f'nums의 합계 :{sum(nums)}')
print(f'nums의 정렬 :{sorted(nums)}, {sorted(nums,reverse=True)}')
print()


# 연산자 ---------------------
## 덧셈
data1 = 11,22
data2 = 'A','B','C'
data3 = data1 + data2
data4 = [1,2]
print(data3)
#곱셈
print(data3 *3)
# print(data3 + data4)
print(data3 + tuple(data4))

# 멤버 연산자 => in , not in 
print(11 in data1)
print('A' in data2)
