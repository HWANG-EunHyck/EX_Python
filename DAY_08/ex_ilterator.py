# -----------------------------------------------------
# Iterator 객체 --> 즉, 반복자를 가지고 있는 객체 : iterable 객체
# 원소를 하나 하나 꺼낼수 있도록 하는 기능
# - 커스텀 클래스 생성 확인
# - 이미 Iterator객체를 가지고 있는 객체들 살펴보기
# -----------------------------------------------------
## 내장함수 dir() :  객체가 가지는 변수와 메서드를 리스트로 알려줌
nums = [11,33,55] # 리스트안에 __iter__가 있다!

# _ 변수 : 저장되는 데이터에 따라서 변수명 지정하는데 
#          이 변수명은 특별한 의미는 없고 문법상 필요한 경우
for _ in dir(nums): 
    print(_)
print()

# 리스트에서 반복자(Iterator) 추출 : __iter__() 메서드
Iterator = nums.__iter__()
print(Iterator.__next__())
print(Iterator.__next__())
print(Iterator.__next__())
print()
## 내장함수 iter(반복이 가능한 객체) : 객체에 존재하는 반복자를 추출

Iterator = iter(nums)
print(Iterator.__next__())
print()

for _ in dir(10): 
    print(_)
print()