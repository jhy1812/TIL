def plane(x,y,z):                                               # 세 점에 의해 정의된 평면이 있으면 법선벡터 반환하는 함수
    vector_1 = [x[0]-y[0], x[1]-y[1], x[2]-y[2]]                # 점x와 점y에 의해 만들어지는 벡터
    vector_2 = [y[0]-z[0], y[1]-z[1], y[2]-z[2]]                # 점y와 점z에 의해 만들어지는 벡터
    
    c = vector_1[0]*vector_2[1]-vector_1[1]*vector_2[0]         # 두 벡터에 모두 수직인 벡터구하는 과정 (법선벡터)
    b = vector_1[0]*vector_2[2]-vector_1[2]*vector_2[0]
    a = vector_1[1]*vector_2[2]-vector_1[2]*vector_2[1]
    
    if a==0 and b==0 and c==0:                                  # 만약 세 값 모두 0이 나오면 오직 하나의 평면이 정의되지 않은 것
        return 1                                                # 따라서 벡터 대신 1 반환
    else:
        return [a, -b, c]                                       # 그렇지 않으면 법선벡터 반환

T = int(input())                                                # 테스트 케이스 수 입력

for i in range(T):
    N = int(input())                                            # 점 개수 입력
    dot = []
    for j in range(N):                                          # 점 개수만큼 점 입력
        dot.append([*map(int,input().split())])
    cnt=0                                                       # 몇 세트의 점 확인했는지 체크해줄 변수
    for j in range(len(dot)-2):                                 # 세 점씩 확인할 것이므로 점 개수에 -2한만큼 반복문
        check = plane(dot[j],dot[j+1],dot[j+2])                 # 순차적으로 평면 정의 되는지 확인
        if check==1:                                            # 1 반환받았으면 확인 개수 1증가시키고 다음 반복문
            cnt+=1
            continue
        else:                                                   # 평면이 정의돼서 법선벡터 반환 받았으면
            break                                               # 반복문 종료
    if cnt==len(dot)-2:                                         # 평면이 계속 정의되지 않아 cnt 확인한 개수만큼 증가했으면 모든 점이 일직선상에 있으므로 잡을 수 있음
        print("#%d TAK" %(i+1))                                 # ->TAK 출력
    else:                                                       # 한 평면이라도 정의 되었으면 진행
        cnt = 0                                                 # 반복문 증가시키며 cnt로 체크하기 위해 cnt 초기화
        for j in range(len(dot)-1):
            if check[0]*dot[j][0]+check[1]*dot[j][1]+check[2]*dot[j][2]!=check[0]*dot[j+1][0]+check[1]*dot[j+1][1]+check[2]*dot[j+1][2]:        # check 변수에 할당된 법선벡터에 의한 평면에 두 점이 모두 존재하는지 체크
                print("#%d NIE" %(i+1))                         # 그렇지 않으면 NIE 출력 후 반복 종료
                break
            else:                                               # 체크하는 두 점이 평면위에 존재하면 cnt 증가
                cnt+=1                            
        if cnt==len(dot)-1:                                     # cnt가 끝까지 증가하여 모든 점이 평면 위에 있으면 TAK 출력
            print("#%d TAK" %(i+1))