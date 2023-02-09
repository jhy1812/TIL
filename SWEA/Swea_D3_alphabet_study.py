T = int(input())

for tc in range(1, T+1):
    moonja = input()
    cnt = 0
    
    for i, j in enumerate(moonja):
        if ord(j)-97 == i:              # 아스키코드 이용해 순서 맞는지 확인
            cnt += 1
        else:
            break
        
    print(f'#{tc} {cnt}')