#----------------------------
# List 데이터 자료형 살펴보기
# - List와 메모리
#----------------------------
# List 생성---------------------
nums = [10,20]
nums1 = list([10,20])

print(nums == nums1) # ==> True

print(f'nums의 id -> {id(nums)}')
print(f'nums의 id[0] -> {id(nums[0])}')
print(f'nums의 id[1] -> {id(nums[1])}')
print('='*30)
print(f'nums1의 id -> {id(nums1)}') # 둘 다 빌 경우 다른 공간에 생성, 단 데이터가 같을 경우 각 원소는 같은 주소를 가짐. 
print(f'nums1[0]의 id -> {id(nums1[0])}')
print(f'nums1[2]의 id -> {id(nums1[1])}')