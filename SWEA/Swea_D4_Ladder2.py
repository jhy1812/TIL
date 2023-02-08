dy = [1, 0, 0]
dx = [0, -1, 1]
 
T = 10
 
for tc in range(1, T+1):
    test_case = int(input())
    N = 100
    mapp = []
    start_spot = []
    minn_index = 0
    minn = 100*2
    for _ in range(N):
        mapp += [[*map(int, input().split())]]
    for i, j in enumerate(mapp[0]):
        if j == 1:
            start_spot += [i]
 
    for i in start_spot:
        y = 0
        x = i
        cnt = 0
        while y != 99:
            if x > 0 and mapp[y][x+dx[1]]:
                while x > 0 and mapp[y][x+dx[1]]:
                    cnt += 1
                    x += dx[1]
                cnt += 1
                y += dy[0]
            elif x < 99 and mapp[y][x+dx[2]]:
                while x < 99 and mapp[y][x+dx[2]]:
                    cnt += 1
                    x += dx[2]
                cnt += 1
                y += dy[0]
            else:
                y += dy[0]
        if minn > cnt:
            minn = cnt
            minn_index = i
    print(f'#{tc} {minn_index}')