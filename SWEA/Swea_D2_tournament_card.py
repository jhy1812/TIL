def tournament(st, ed):                     # 재귀 (그룹 나눌 시작 인덱스, 마지막 인덱스)
    if ed - st <= 1:                        # 두명 이하 그룹이면 가위바위보해서 승자 반환
        if card[st] == card[ed]:
            return st
        elif card[st] - card[ed] == 1:
            return st
        elif card[st] - card[ed] == -2:
            return st
        else:
            return ed
 
    new_st = tournament(st, (st+ed)//2)      # 1번 그룹 토너먼트  (**새로운 변수가 아닌 st 변수 그대로 사용하면
    new_ed = tournament((st+ed)//2+1, ed)    # 2번 그룹 토너먼트   함수 들어갈 때 원래 st가 아닌 바뀐 st 들어가버림)
 
    if card[new_st] == card[new_ed]:         # 가위바위보해서 승자 반환
        return new_st
    elif card[new_st] - card[new_ed] == 1:
        return new_st
    elif card[new_st] - card[new_ed] == -2:
        return new_st
    else:
        return new_ed
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    card = [*map(int, input().split())]
    winner = tournament(0, N-1) 
    print(f'#{tc} {winner+1}')              # 인덱스에 1 더한 값 반환