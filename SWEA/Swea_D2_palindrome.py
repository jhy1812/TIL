def row_check(y, x, lst, M, N):
    cnt = 0
    result = ''
    if x+M-1 >= N:
        return 1
    for i in range(M):
        if lst[y][x+i] == lst[y][x+M-i-1]:
            result += lst[y][x+i]
            cnt += 1
    if cnt != M:
        return 1
    else:
        return result
 
def col_check(y, x, lst, M, N):
    cnt = 0
    result = ''
    if y+M-1 >= N:
        return 1
    for i in range(M):
        if lst[y+i][x] == lst[y+M-i-1][x]:
            result += lst[y+i][x]
            cnt += 1
    if cnt != M:
        return 1
    else:
        return result
 
 
T = int(input())
 
for tc in range(1, T+1):
    N, M = [*map(int, input().split())]
    gljapan = []
    for i in range(N):
        gljapan += [input()]
    result = ''
    for i in range(N):
        for j in range(N):
            if row_check(i, j, gljapan, M, N) != 1:
                result = row_check(i, j, gljapan, M, N)
                break
            elif col_check(i, j, gljapan, M, N) != 1:
                result = col_check(i, j, gljapan, M, N)
                break
        if result != '':
            break
    print(f'#{tc} {result}')