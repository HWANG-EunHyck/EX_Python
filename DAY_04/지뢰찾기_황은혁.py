# [['.', '*', '*'], ['*', '.', '.'], ['.', '*', '.']]
# 가로 세로




col, row = list(map(int, input().split()))

matrix = []
for i in range(row):
    matrix.append(list(input()))

print(matrix)
# col = 3
# row = 3

# matrix = [['.', '*', '*'], ['*', '.', '.'], ['.', '*', '.']]

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            print(matrix[i][j], sep='', end='')
        else:
            cnt = 0
            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    if a < 0 or b < 0 or a >= row or b >= col:
                        continue
                    elif matrix[a][b] == '*':
                        cnt += 1
            print(cnt, end='', sep='')
    print()

# data = input("주민등록번호를 입력하세요 (형식: XXXXXX-XXXXXXX): ")

# gender = data.split('-')[1][0]
# print(data.split('-')[1])


# if gender == '1' or gender == '3':
#     print("남자")
# elif gender == '2' or gender == '4':
#     print("여자")
# else:
#     print("잘못된 주민등록번호입니다.")


# def check_gender(gender_number):
    
#     gender = gender_number[7]
    
    
#     if gender in ['1', '3']:
#         return "남자"
#     elif gender in ['2', '4']:
#         return "여자"
#     else:
#         return "잘못된 주민등록번호입니다."

# gender_number = input("주민등록번호를 입력하세요 (예: 821010-1635210): ")

# print(check_gender(gender_number))


# 
# 예
# 입력
# 76 82 89 84
# 결과
# 낮은 점수: 76.00, 높은 점수: 89.00, 평균 점수: 82.75
# 낮은 점수: 82.00, 높은 점수: 84.00, 평균 점수: 83.00