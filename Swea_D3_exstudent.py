# TC = int(input())

# for i in range(TC):
#     n = int(input())
#     week = [*map(int,input().split())]
#     lecture_day=[]
#     for j in range(len(week)):
#         if week[j]==1:
#             lecture_day.append(j+1)
            

#     if len(lecture_day)==1:
#         print("#%d %d" %(i+1, (n-1)*7+1))
#     else:
#         m=n%len(lecture_day)+len(lecture_day)
#         base=(n-m)//len(lecture_day)*7
#         lecture_day_rev=[]
#         lecture=[]
#         for i in range(len(lecture_day)):
#             lecture_day_rev.append(8-lecture_day[i])
#         lecture.extend(lecture_day_rev)
#         lecture.extend(lecture_day)
#         check=[]
#         for i in range(len(lecture)-m):
#             check.append(lecture[i]+lecture[i+m-1])
#         print("#%d %d" %(i+1,base+min(check)))
    
    
    # m=n%len(lecture_day)+len(lecture_day)
    # l=(n-m)//len(lecture_day)*7
    # lecture_day_rev=[]
    # lecture=[]
    # for i in range(len(lecture_day)):
    #     lecture_day_rev.append(8-lecture_day[i])
    # lecture.extend(lecture_day_rev)
    # lecture.extend(lecture_day)
    # check=[]
    # for i in range(len(lecture)-m):
    #     check.append(lecture_day[i]+lecture_day[i+m-1])
    # print(l+min(check))
    
    
    
        # if n%len(lecture_day)==0:
    #     N=(n//(len(lecture_day))-1)*7+lecture_day[len(lecture_day)-1]+1
    # else:
    #     N=n//(len(lecture_day))*7+lecture_day[n%len(lecture_day)-1]+1
    # print("#%d %d" %(i+1, N))
    
    
    # check=[]
    # for j in range(7):
    #     cnt=0
    #     while cnt!=n:
    #         for k in week:
    #             if k==1:
    #                 cnt+=1
    #     check.append(cnt)
    # print("#%d %d" %(i+1, min(check)))
    
TC = int(input())

for i in range(TC):
    n = int(input())
    week = [*map(int,input().split())]
    lecture_day = []
    check = []
    for j in range(len(week)):
        days = 0
        cnt = 0
        if week[j] == 1:
            lecture_day = week[j:]+week[:j]
            while True:
                for k in range(len(lecture_day)):
                    days +=1
                    if lecture_day[k] == 1:
                        cnt+=1
                    if cnt == n:
                        break
                if cnt == n:
                    break
        else:
            continue

        check.append(days)
    print('#%d %d'%(i+1,min(check)))