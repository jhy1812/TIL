T = int(input())

for i in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    if N%2 == 1:
        cnt = 1
        for j in range((N+1)//2):
            if j != (N+1)//2-1:
                for k in range(4):
                    if k == 0:
                        for m in range(j, N-1-j):
                            arr[j][m] = cnt
                            cnt+=1
                    elif k == 1:
                        for m in range(j, N-1-j):
                            arr[m][N-1-j] = cnt
                            cnt+=1
                    elif k == 2:
                        for m in range(j, N-1-j):
                            arr[N-j-1][N-1-m] = cnt
                            cnt+=1
                    else:
                        for m in range(j, N-1-j):
                            arr[N-1-m][j] = cnt
                            cnt+=1 
            else:
                arr[j][j] = cnt
    else:
        cnt = 1
        for j in range(N//2):
            for k in range(4):
                if k == 0:
                    for m in range(j, N-1-j):
                        arr[j][m] = cnt
                        cnt+=1
                elif k == 1:
                    for m in range(j, N-1-j):
                        arr[m][N-1-j] = cnt
                        cnt+=1
                elif k == 2:
                    for m in range(j, N-1-j):
                        arr[N-j-1][N-1-m] = cnt
                        cnt+=1
                else:
                    for m in range(j, N-1-j):
                        arr[N-1-m][j] = cnt
                        cnt+=1
    print("#%d" %(i+1))
    for i in range(len(arr)):
        print(*arr[i])