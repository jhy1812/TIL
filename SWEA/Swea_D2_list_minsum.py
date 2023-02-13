def get_sum(level, N, sum):
    global minn
    if minn < sum:
        return
    if level == N:
        if minn > sum:
            minn = sum
        return
    for i in range(N):
        if i in path:
            continue
        path.append(i)
        sum += numbers[level][i]
        get_sum(level + 1, N, sum)
        path.pop()
        sum -= numbers[level][i]
         
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    numbers = []
    for i in range(N):
        numbers.append([*map(int, input().split())])
    minn = 21e5
    path = []
    get_sum(0, N, 0)
    print(f'#{tc} {minn}')