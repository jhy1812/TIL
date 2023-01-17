T=10

for i in range(T):
    N = int(input())
    building = [*map(int,input().split())]
    floar = 0
    for j in range(2, len(building)-2):
        dif=[]
        if building[j]-building[j-1]>0:
            dif.append(building[j]-building[j-1])
            if building[j]-building[j-2]>0:
                dif.append(building[j]-building[j-2])
                if building[j]-building[j+1]>0:
                    dif.append(building[j]-building[j+1])
                    if building[j]-building[j+2]>0:
                        dif.append(building[j]-building[j+2])
                        floar+=min(dif)
                else:
                    continue
            else:
                continue
        else:
            continue
    print("#%d %d" %(i+1, floar))