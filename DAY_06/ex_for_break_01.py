#-------------------------------------------------------------------
# 제어문 - 반복문 중단 break
# - 반복을 중단 시키는 조건문과 함께 사용 됨
# ------------------------------------------------------------------
## [실습] 숫자 데이터의 합계가 30이상이되면 더 이상 합계를 하지 마세요. 숫자 데이터는 1~50으로 구성됨
# ------------------------------------------------------------------

# sum = 0
# for i in range(1,51):
#     if sum>=30:
#         su = i-1
#         break
#     sum += i

# print(sum,su)

# ------------------------------------------------------------------
## [실습] 4개 과목점수가 있습니다.
##        과목점수가 40이하면 불합격입니다.
##        4개 과목 평균이 60점 이상이면 합격입니다.
# ------------------------------------------------------------------

jumsu =[89,41,80,77]
isPass = True

for i in jumsu:
    if i<40:
        print('과락입니다.')
        isPass = False
        break


if isPass:
    avg = sum(jumsu)/len(jumsu)
    if avg>=60:
        print(f'당신은 {avg}로 합격입니다')
    else:
        print(f'당신은 {avg}로 불합격입니다')
else:
    print('당신은 40미만인 과목으로 불합격입니다.')
        

