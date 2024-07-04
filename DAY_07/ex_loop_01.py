# ## [1] outer = 5 , inner = 5
# for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
#     for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
#         print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
#     print('i:', i, '\n', sep='')

for i in range(5):
    print(' '*i + '*')

for i in range(5):
    for n in range(i+1):
        # if i == n :
        #     print('*',end = '\n')
        # else:
        #     print(' ',end='')
        print('*',end='\n') if i ==n else print(' ',end='')

for i in range(5):
    for j in range(5):
        if j>=i:
            print('*',end='')                                                                   
    print()

num = int(input())

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * (2 * i - 1))

