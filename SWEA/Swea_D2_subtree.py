def dfs(now):
    global cnt
    cnt += 1
    for i in range(E+2):
        if arr[now][i] == 1:
            dfs(1)

T = int(input())

for tc in range(1, T+1):
    E, N = [*map(int, input().split())]     # E-간선 개수, N-루트 노드
    arr = [[0 for _ in range(E+2)] for _ in range(E+2)]
    node_info = [*map(int, input().split())]
    cnt = 0

    for i in range(0, 2*E-1, 2):
        arr[node_info[i]][node_info[i+1]] = 1
    
    dfs(N)
    print(cnt)