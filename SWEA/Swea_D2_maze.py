from collections import deque
 
def maze(y, x):
    queue = deque()
    queue.append((y,x))
    visit[y][x] = True
    while 1:
        now = queue.popleft()
        for k in range(4):
            y = now[0] + dy[k]
            x = now[1] + dx[k]
            if 0 <= y < N and 0 <= x < N:
                if mapp[y][x] != '1' and not visit[y][x]:
                    queue.append((y, x))
                    visit[y][x] = True
        if len(queue) == 0:
            return
 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    mapp = []
    for _ in range(N):
        mapp.append(list(input()))
    visit = [[False for _ in range(N)] for _ in range(N)]
    sty, stx = 0, 0
    edy, edx = 0, 0
    for i in range(N):
        for j in range(N):
            if mapp[i][j] == '2':
                sty, stx = i, j
            if mapp[i][j] == '3':
                edy, edx = i, j
    maze(sty, stx)
 
    if not visit[edy][edx]:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')