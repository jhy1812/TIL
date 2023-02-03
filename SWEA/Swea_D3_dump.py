T = 10

for i in range(10):
    dump = int(input())
    box = [*map(int,input().split())]

    for j in range(dump):
        box[box.index(max(box))]+=-1
        box[box.index(min(box))]+=1
        
        if max(box)-min(box)<=1:
            print("#%d %d" %(i+1, max(box)-min(box)))
            break
    print("#%d %d" %(i+1, max(box)-min(box)))