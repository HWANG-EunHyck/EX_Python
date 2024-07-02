#-------------------------------------------------
#  set 자료형 살펴보기 (중복제거용)
# - 여러가지 종류의 여러 개 데이터를 저장
# - 단! 중복 안됨!!
# - 컬렉션 타입의 데이터 저장 시 Tuple 가능(list X)
# - 형태 : (데1,데2,...,데n)
#-------------------------------------------------
## [set 생성]------------------------------------
data = []
data = ()
data = {}
data = set()

print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')

print()

# 여러개 데이터 저장한 set
data = {10,20,30,-9,10,20,30,10,10}
print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
print()

data = {9.34,'apple',True,10,'10'}
print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
print()

# data = {1,2,3,[1,2,3]}
# 리스트는 요소로 불가능
data = {1,2,3,(1,2,3)}
data = {1,2,3,(1)}
data = {1,2,3,(1,)[0]}
print(f'data의 타입: {type(data)}, 원소/요소 개수 : {len(data)}개, 데이터 : {data}')
print()

# data2 = {1,2,3,data}
# data = {1,2,3,{1:100}}
# 둘 다 변경 가능한 형태라 불가능

# set() 내장함수 : 생성자 메서드
data = {1,2,3} # ===> set([1,2,3])
data = set() # ===> empty set
data = set({1,2,3})

# 다양한 타입 ====> set 변환 
data = set({'name': '홍길동','age' : 12})
data = set('Good') ;print(data)
data = set({'name': '홍길동','age' : 12}) ;print(data)

