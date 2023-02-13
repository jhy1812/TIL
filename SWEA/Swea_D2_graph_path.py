T = int(input())

for tc in range(1, T+1):
    V, E = [*map(int, input().split())]
    node = [[] for _ in range(V+1)]
    visit = [False]*(V+1)

    for i in range(E):
        s, e = [*map(int, input().split())]
        node[s].append(e)
        node[e].append(s)
    st, ed = [*map(int, input().split())]

    def search(v):
        visit[v] = True
        for i in node[v]:
            if not visit[i]:
                search(i)
    search(st)
    if visit[ed] == False:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')