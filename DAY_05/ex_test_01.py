#-----------------------------------------
# [실습1] 글자를 입력받습니다
#         입력 받은 글자의  (a~z, A~Z) 코드값을 출력 합니다.
#-----------------------------------------

alp = input()

if alp.isalpha() and len(alp) == 1:
    print(ord(alp))
else:
    print('유효한 입력이 아닙니다')

#-----------------------------------------
# [실습1] 점수를 입력 받은 후 학점을 출력합니다
# - 학점 : A+,  A,  A-,  B+,B,B-,C+,C,C-,D+,D,D-,F
#       100~96 95 94~90
#-----------------------------------------

jumsu = int(input())

if 100>=jumsu>=0 :
    if 100>= jumsu>=96:
        print('A+')
    elif jumsu == 95:
        print('A')
    elif jumsu>=90:
        print('A-')
    elif jumsu>=86:
        print('B+')
    elif jumsu == 85:
        print('B')
    elif jumsu>=80:
        print('B-')
    elif jumsu>=76:
        print('C+')
    elif jumsu == 75:
        print('C')
    elif jumsu>=70:
        print('C-')
    elif jumsu>=66:
        print('D+')
    elif jumsu == 65:
        print('D')
    elif jumsu>=60:
        print('D-')
    else:
        print('F')
else:
    ('잘못된 입력입니다.')