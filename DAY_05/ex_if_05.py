# ----------------------------------------------------------
# 조건부 표현식
# ----------------------------------------------------------
## [실습] 문자 1개 코드값을 저장하는 조건식을 작성
## - 알파벳(a~z,A~Z) 코드값으로 변환
## - 그 외는 None으로 코드값으로 전달
alp = input()

num = ord(alp) if 'a'<=alp<='z' or 'A'<=alp<='Z' else None

print(num)
