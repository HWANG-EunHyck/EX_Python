#----------------------------
# Dict 자료형 살펴보기
# - 데이터의 의미를 함꼐 저장하는 자료형
# - 형태 : {키:값,...키n:값n}
# - 키는 중복 x , 값은 중복 o
# - 데이터 분석 시 파일 데이터 가져 올 떄 많이 사용
#----------------------------
## [Dict 생성]
data = {}
print(f'data = {len(data)}개, {type(data)}, {data}')

# 사람에 대한 정보: 이름, 나이, 성별
data ={'name' : '마징가','age' : 100, 'gender': '남'}
data = dict(zip(['name','마징가','gender'],['마징가',100,'남']))
print(f'data = {len(data)}개, {type(data)}, {data}')

# 강아지에 대한 정보 : 품종,무게 색상 성별 나이
data = dict(zip(['kind','weight','color','gender','age',],['cz','5kg','rainbow','female',25]))
print(f'data = {len(data)}개, {type(data)}, {data}')

## [Dict 원소/요소 읽기]------
## - 키를 가지고 값/데이터 읽기
## - 형식 : 변수명[키]

data = dict(zip(['kind','weight','color','gender','age',],['cz','5kg','rainbow','female',25]))

# 색상 출력
print(f'{data["color"]}')

# 성별 ,품종 출력
print(f'{data["gender"]},{data["kind"]}')

## [Dict 원소/요소 변경]------
# - 변수명[키] =  새로운 값
# 나이 5살 ==> 6살
data['age'] = '6'
print(f'data = {len(data)}개, {type(data)}, {data}')
data['weight'] = '8kg'
print(f'data = {len(data)}개, {type(data)}, {data}')

## - del 변수명[키] 또는 del(변수명[키])
## 성별 데이터 삭제
del data['kind']
print(f'data = {len(data)}개, {type(data)}, {data}')

## - 변수명[새로운 키] = 값 -------------
## 이름 추가
data['name'] = '글라스'
print(f'data = {len(data)}개, {type(data)}, {data}')