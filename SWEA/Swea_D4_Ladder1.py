T = 10
 
for tc in range(1, T+1):
    num = int(input())
    sadari = []
    for i in range(100):
        sadari += [[0]+[*map(int, input().split())]+[0]]
    start_spot = 0
    cnt = 0
    for i in sadari[99]:                                 
        if i == 2:
            start_spot = cnt
            break
        cnt += 1
    y = 99
    x = start_spot
    while 1:
        if sadari[y][x-1] == 1:
            while 1:
                x -= 1
                if sadari[y][x-1] != 1:
                    break
            y -= 1
        elif sadari[y][x+1] == 1:
            while 1:
                x += 1
                if sadari[y][x+1] != 1:
                    break
            y -= 1
        else:
            y -= 1
        if y == 0:
            break
    print(f'#{tc} {x-1}')