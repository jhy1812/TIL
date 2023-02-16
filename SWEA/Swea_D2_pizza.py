from collections import deque

def baking(N, M):
    pizza = deque()
    indexx = deque()
    i = 0
    while 1:
        if i < M:
            if len(pizza) < N:
                pizza.appendleft(cheeze[i])
                indexx.appendleft(i)
                i += 1
            else:
                while 1:
                    pizza.appendleft(pizza.pop()//2)
                    indexx.appendleft(indexx.pop())
                    if pizza[0] == 0:
                        pizza.popleft()
                        pizza.appendleft(cheeze[i])
                        indexx.popleft()  
                        indexx.appendleft(i)
                        i += 1
                        if i == M:
                            break
        if i == M:
            while 1:
                pizza.appendleft(pizza.pop()//2)
                indexx.appendleft(indexx.pop())
                if pizza[0] == 0:
                    pizza.popleft()
                    indexx.popleft()
                if len(pizza) == 1:
                    break
            break
    result = indexx.popleft()
    return result
            
T = int(input())

for tc in range(1, T+1):
    N, M = [*map(int, input().split())] # N - 화덕크키, M - 피자 개수
    cheeze = [*map(int, input().split())]
    result = baking(N, M)
    print(f'#{tc} {result+1}')