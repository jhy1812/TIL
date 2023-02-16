def dfs(st):
    global sum
    if arr[st] == [0]*(N+1):
        sum += node_num[st]
        return
    for i in range(N+1):
        if arr[st][i] == 1:
            dfs(i)


T = int(input())

for tc in range(1, T+1):
    N, M, L = [*map(int, input().split())]      # N-노드개수, M-리프노드 개수, L-출력할노드
    node_info = [0]*M

    for i in range(M):
        node_info[i] = [*map(int, input().split())]
    node_num = [0]*(N+1)
    for i in node_info:
        node_num[i[0]] = i[1]

    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

    i = 1
    j = 2
    cnt = 1
    while 1:
        arr[i][j] = 1
        cnt += 1
        if cnt == N:
            break
        arr[i][j+1] = 1
        cnt += 1
        i += 1
        j += 2
        if cnt == N:
            break
    sum = 0
    dfs(L)
    print(f'#{tc} {sum}')