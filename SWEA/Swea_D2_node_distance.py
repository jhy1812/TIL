from collections import deque
 
def search(st, ed):
    global count
    queue = deque()
    queue.append(nodes[st])
    visited[st] = True
    while queue:
        now = queue.popleft()
        check = []
        for i in now:
            if not visited[i]:
                visited[i] = True
                check.extend(nodes[i])
        queue.append(check)
        count += 1
        if len(check) == 0:
            return
        if visited[ed]:
            return
 
T = int(input())
 
for tc in range(1, T+1):
    V, E = [*map(int, input().split())]
    nodes = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    check = [0]*(V+1)
 
    for _ in range(E):
        s, e = [*map(int, input().split())]
        nodes[s].append(e)
        nodes[e].append(s)
    st, ed = [*map(int, input().split())]
    count = 0
    search(st, ed)
 
    if not visited[ed]:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {count}')