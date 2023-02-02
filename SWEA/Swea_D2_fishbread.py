def ssort(lst):
    maxx = lst[0]
    for i in lst:
        if maxx < i:
            maxx = i
    bucket = [0]*(maxx+1)
    
    leng = 0
    for i in lst:
        bucket[i] += 1
        leng += 1

    cnt = 0
    for _ in bucket:
        cnt += 1
    
    sum = 0
    for i in range(cnt):
        sum += bucket[i]
        bucket[i] = sum
    
    result = [0]*leng

    for i in lst:
        result[bucket[i]-1] = i
        bucket[i] -= 1
    return result

T = int(input())

for tc in range(1, T+1):
    N, M, K = [*map(int, input().split())]
    people = [*map(int, input().split())]
    check = 0
    people = ssort(people)
    for i in range(N):
        if (people[i]//M)*K < i+1:
            print(f'#{tc} Impossible')
            check += 1
            break
    if check == 0:
        print(f'#{tc} Possible')


    