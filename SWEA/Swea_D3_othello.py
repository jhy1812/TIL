def col_check(x, y, color):                 # 방향배열 0~1
    for i in range(2):
        flag = 0
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < N and 0 <= new_x < N:
            if mapp[new_y][new_x] != color and mapp[new_y][new_x] != 0:
                while 1:
                    new_y += dy[i]
                    new_x += dx[i]
                    if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                        break
                    else:
                        if mapp[new_y][new_x] == 0:
                            break
                        elif mapp[new_y][new_x] == color:
                            flag += 1
                            break
                        else:
                            continue
        if flag == 1:
            if new_y >= y+dy[i]:
                for j in range(y+dy[i], new_y):
                    mapp[j][x] = color
            else:
                for j in range(y+dy[i], new_y, -1):
                    mapp[j][x] = color
 
def row_check(x, y, color):                 # 방향배열 2~3
    for i in range(2, 4):
        flag = 0
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < N and 0 <= new_x < N:
            if mapp[new_y][new_x] != color and mapp[new_y][new_x] != 0:
                while 1:
                    new_y += dy[i]
                    new_x += dx[i]
                    if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                        break
                    else:
                        if mapp[new_y][new_x] == 0:
                            break
                        elif mapp[new_y][new_x] == color:
                            flag += 1
                            break
                        else:
                            continue
        if flag == 1:
            if new_x >= x+dx[i]:
                for j in range(x+dx[i], new_x):
                    mapp[y][j] = color
            else:
                for j in range(x+dx[i], new_x, -1):
                    mapp[y][j] = color
 
def cross_check(x, y, color):               # 방향배열 4~7
    for i in range(4, 8):
        cnt = 1
        flag = 0
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < N and 0 <= new_x < N:
            if mapp[new_y][new_x] != color and mapp[new_y][new_x] != 0:
                while 1:
                    new_y += dy[i]
                    new_x += dx[i]
                    if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                        break
                    else:
                        if mapp[new_y][new_x] == 0:
                            break
                        elif mapp[new_y][new_x] == color:
                            flag += 1
                            break
                        else:
                            cnt += 1
                            continue
        if flag == 1:
            for j in range(cnt):
                mapp[y+dy[i]*(j+1)][x+dx[i]*(j+1)] = color
 
T = int(input())
 
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]
for tc in range(1, T+1):
    N, M = [*map(int, input().split())]
    mapp = [[0 for _ in range(N)] for _ in range(N)]
    mapp[N//2-1][N//2-1], mapp[N//2][N//2] = 2, 2
    mapp[N//2][N//2-1], mapp[N//2-1][N//2] = 1, 1
    chaksu = [0]*M
    for i in range(M):
        chaksu[i] = [*map(int, input().split())]
    for i in range(M):
        mapp[chaksu[i][1]-1][chaksu[i][0]-1] = chaksu[i][2]
        col_check(chaksu[i][0]-1, chaksu[i][1]-1, chaksu[i][2])
        row_check(chaksu[i][0]-1, chaksu[i][1]-1, chaksu[i][2])
        cross_check(chaksu[i][0]-1, chaksu[i][1]-1, chaksu[i][2])
    w_sum = 0
    b_sum = 0
    for i in range(N):
        for j in range(N):
            if mapp[i][j] == 2:
                w_sum += 1
            elif mapp[i][j] == 1:
                b_sum += 1
    print(f'#{tc} {b_sum} {w_sum}')