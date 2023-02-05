TC = int(input())                                           # 테스트 케이스 개수 입력                  

for i in range(TC):                                         # 테스트 케이스만큼 반복
    n = int(input())                                        # 목표 수업 일수 n 입력
    week = [*map(int,input().split())]                      # 일주일간 수업 정보 입력 (수업 열리면 1, 아니면 0)
    lecture_day = []                                        
    check = []                                              # 시작 요일에 따라 지내야 하는 일수 입력받을 리스트 선언
    for j in range(len(week)):                              
        days = 0                                            # 지내는 일수 입력받을 변수
        cnt = 0                                             # 수업 받는 일수 입력받을 변수
        if week[j] == 1:                                    # @@수업이 있는 날부터 지내야 최소 일수를 구할 수 있으므로, 수업 정보가 1일 때 반복 시작
            lecture_day = week[j:]+week[:j]                 # 수업이 있는 날로 시작하는 리스트 할당
            while True:                                             
                for k in range(len(lecture_day)):           # 일주일 분량만큼 반복 
                    days +=1                                # 지내는 일수는 조건 없이 반복될 때마다 +1
                    if lecture_day[k] == 1:                 # 만약 수업이 열린다면 수업 받는 일수 +1
                        cnt+=1                              
                    if cnt == n:                            # 만약 수업 받은 일수가 목표 일수와 같아지면 for문 종료
                        break
                if cnt == n:                                # 위와 같은 조건 만족시 while문 종료
                    break
        else:                                               # @@
            continue

        check.append(days)
    print('#%d %d'%(i+1,min(check)))