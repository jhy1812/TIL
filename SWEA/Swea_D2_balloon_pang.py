dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

def cross_check(y, x, lst, N, M):
    sum = 0
    for i in range(5):
        if 0 <= y+dy[i] < N and 0 <= x + dx[i] < M:
            sum += lst[y+dy[i]][x+dx[i]]
    return sum

T = int(input())

for tc in range(1, T+1):
    N, M = [*map(int, input().split())]
    mapp = []
    for _ in range(N):
        mapp += [[*map(int, input().split())]]
    maxx = cross_check(0, 0, mapp, N, M)
    
    for i in range(N):
        for j in range(M):
            if maxx < cross_check(i, j, mapp, N, M):
                maxx = cross_check(i, j, mapp, N, M)
                
    print(f'#{tc} {maxx}')