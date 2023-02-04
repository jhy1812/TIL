T = int(input())                                  
                                                  
for tc in range(1, T+1):                          
    K, N, M = [*map(int, input().split())]        
    line = [*map(int, input().split())]           
    line = [0] + line + [N]                       
    charge = 0                                    
    dis = 0                                       
    check = 0                                     
    for i in range(M+1):                          
        dis += line[i+1] - line[i]                
        if line[i+1] - line[i] > K:               
            print(f'#{tc} 0')                     
            check = -10                           
            break                                 
        if dis == K:                              
            check = dis                           
            charge += 1                           
            dis = 0                               
        elif dis > K:                             
            check = dis                           
            charge += 1                           
            dis = line[i+1] - line[i]
    if dis > 0 and dis < K:
        check = 0             
    if check == K:                                
        charge -= 1                               
    if check != -10:                              
        print(f'#{tc} {charge}')  