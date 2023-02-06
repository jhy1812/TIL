T = int(input())                                            # 테스트 케이스

for i in range(T):
    day = int(input())                                      # 원재가 매매가 예측할 수 있는 일수 입력
    
    expense = [*map(int,input().split())]                   # 매매가 정보 입력
    
    money = 0                                               # 얼마 벌 수 있는지 입력 받을 변수
    while len(expense) != 0:                                # 예측가능한 매매가가 없어질 때까지 반복
        maxx = max(expense)                                 # 예측가능한 매매가 중 최대값 반환
        if expense[0] == maxx:                              # 예측가능 매매가 중 첫날의 매매가가 최대값이면 
            del expense[0]                                  # 첫날 매매가 삭제
        else:                                               # 그렇지 않으면
            cnt = 0
            for j in range(expense.index(maxx)):            # 최대값 있는 날까지 반복
                money += maxx - expense[j]                  # 각 날의 매매가와 최대 매매가의 차이만큼 증가
                cnt = j                                     # 최대값 있는 날이 언제인지 반환
            expense = expense[j+1:]                         # 최대값 있는 날까지 매매가 정보 삭제

    print('#%d %d' %(i+1,money))                            # 벌 수 있는 돈 출력