#----------------------------------------------
# Tuple 전용 함수 즉 ,메서드
# - 수정 불가 즉, 추가 ,삭제 , 변경 x
# ---------------------------------------------

nums = 10,20,30

## 메서드 - 인덱스 확인 메서드 index(데이터)

idx = nums.index(20)

print(idx)

if 4 in nums:
    print(nums.index(4))


## 메서드 - 데이터 갯수 확인 메서드 count(데이터)
print(10,'은 :',nums.count(10)+'개')
print(5,'은 :',nums.count(5)+'개')
