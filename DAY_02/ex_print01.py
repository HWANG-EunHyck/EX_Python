#-----
# 내장함수 print() 사용법
# - 모니터 즉, 콜솔/터미널에 출력하는 함수
# - 문법 : print(argument,...,n) 
# -        print( )   
#----- 
# 나이, 이름, 성별을 저장하기
age = 100
name = '홍동길'
gender = 'male'

# 모니터에 출력하기
print(age,end= 'g')

# 한줄에 세개 모두 출력하기
print(age , name , gender,sep = '-')

# 두개의 정수 덧셈 결과 출력하기 (정수 %d , 실수 %f , 문자열 %s)
# ==> 서식 지정자 (format strion) 방식
# ==> 화면 출력 글자를 만들고 그 글자안에 특정결과를 출력하는 형식
# ==> 글자 내부에 정수 결과 넣기: '   %d '%(변수명or수식)
# ==> 글자 내부에 실수 결과 넣기: '   %f '%(변수명or수식)
# ==> 글자 내부에 글자 결과 넣기: '   %s '%(변수명or수식)

a= 10
b= 20
print('%d + %d = %d' %(a,b,a+b))
print('a+b = %d \naXb = %d'%(a+b,a*b))


# 9 / 2 = 4.5
a= 9
b= 2
print('%d / %d = %f'%(a,b,a/b))
print('%s / %s = %s'%(a,b,a/b))

# ==> f-string 방식
# ==> 형식 : f'  {변수명 or 수식 or 데이터}   '
# ==> 형식 : F'  {변수명 or 수식 or 데이터}   ' 
print(f'{a} + {b} = {a+b}')
print(f'{a} / {b} = {a/b}')