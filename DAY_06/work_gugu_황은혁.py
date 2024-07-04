# [1] 구구단 전체 출력 => 중첩 for ==> for 1개로

for i in range(72):
    n = 2+i//9
    m = 1+i%9
    print(f'{n} * {m} = {n*m}')


# [2] 구구단 가로 출력
for i in range(1,10):
    for n in range(2,6):
        print(f'{n} * {i} = {i*n}',end='\t')
    print()
for i in range(1,10):
    for n in range(6,10):
        print(f'{n} * {i} = {i*n}',end='\t')
    print()
