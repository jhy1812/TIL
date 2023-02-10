def row_check(y, x, lst, N, K):
    cnt = 0
    if x+K-1 > N-1:
        return -1
    for i in range(K):
        if lst[y][x+i] == lst[y][x+K-i-1]:
            cnt += 1
    if cnt != K:
        return -1
    else:
        return K    
def col_check(y, x, lst, N, K):
    if y+K-1 > N-1:
        return -1
    for i in range(K):
        if lst[y+i][x] != lst[y+K-i-1][x]:
            return -1
    return K    
 
T = 10
 
for tc in range(1, T+1):
    test_case = int(input())
    N =100
    gljapan = []
    for _ in range(N):
        gljapan += [input()]
    result = 0
    for i in range(100, 1, -1):
        for j in range(N):
            for k in range(N):
                result = row_check(j, k, gljapan, N, i)
                if result != -1:
                    break
                result = col_check(j, k, gljapan, N, i)
                if result != -1:
                    break
            if result != -1:
                break
        if result != -1:
            break
    if result == -1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} {result}')