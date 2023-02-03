TC = int(input())

for i in range(TC):
    n = int(input())
    week = [*map(int,input().split())]
    lecture_day=[]
    for j in range(len(week)):
        if week[j]==1:
            lecture_day.append(j+1)
            

    if len(lecture_day)==1:
        print("#%d %d" %(i+1, (n-1)*7+1))
    else:
        m=n%len(lecture_day)+len(lecture_day)
        base=(n-m)//len(lecture_day)*7
        lecture_day_rev=[]
        lecture=[]
        for j in range(len(lecture_day)):
            lecture_day_rev.append(8-lecture_day[j])
        lecture.extend(lecture_day_rev)
        lecture.extend(lecture_day)
        check=[]
        if n%len(lecture_day) != 0:
            for j in range(len(lecture)-m+1):
                check.append(lecture[j]+lecture[j+m-1])
            print("#%d %d" %(i+1,base+min(check)))
        else:
            check.append(lecture[0])
            check.append(lecture[-1])
            for j in range(len(lecture)-m+1):
                check.append(lecture[j]+lecture[j+m-1])
            print("#%d %d" %(i+1,base+min(check)))