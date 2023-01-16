a=3
print(id(a))
b=a
print(id(b))

'''
변수
연산자
자료형 형변환
컨테이너들 (리스트 튜플 range// set 딕셔너리)
'''

# 변수
a=3
b=5
print(f"{a} + {b} = {a+b}입니다")
print("{0} + {1} = {2}입니다".format(a,b,a+b))

# swap
a=3
b=5
temp=a
a=b
b=temp

# 자료형
a=3
print(type(a))
a=3.14
print(type(a))
print(round(a,1))
print(f"{a:.1f}")

a=5
a=str(a) #"5"
print(a)
print(type(a))

print("오늘은 \"100%\" \n입니다")

# slicing
s="abcdefg"
print(s[:3])        # 맨 앞에서부터 3번 인덱스 전까지
print(s[3:])        # 3번 인덱스부터 끝까지
print(s[2:5])       # 2번 인덱스부터 5번 인덱스 전까지
print(s[5:2:-1])    # 5번 인덱스부터 2번 인덱스보다 클 때까지 -1씩
print(s[1:5:2])     # 1번 인덱스부터 5번 인덱스 전까지 +2씩

# boolean
a,b=0,-1                # 0-False   0 이외-True
a,b=bool(a),bool(b)
print(a,b)

# list
lst=[1,2,3,4,5]
print(lst)
print(*lst)
print(type(lst))

print(lst[1])
print(len(lst))
print(lst[-1])

# 튜플
tp=(1,2,3,4,5)
print(tp)
print(type(tp))
print(len(tp))
print(tp[-1])

# range
print(list(range(3)))
print(list(range(1,5)))

# set - 리스트에서 중복된것 제거
lst=[2,1,5,6,8,8,3,2,5,4,8,3,2,1,5,5,6]
lst=list(set(lst))
print(lst)

# 딕셔너리

# N=int(input())
# lst=[[0 for i in range(4)] for j in range(4)]
# for i in range(4):
#     for j in range(4):
#         if i%2==0:
#             lst[i][j]=N
#             N+=1
#         else:
#             lst[i][len(lst)-j-1]=N
#             N+=1    
# for i in range(len(lst)):
#     print(*lst[i])


# arr=["A","P","P","L","E","T"]
# lst=input().split()
# cnt=0
# for i in arr:
#     for j in lst:
#         if i==j:
#             cnt+=1
# print("%d개 맞추었습니다" %cnt)

# arr=[['F','R','Q','W','T'],['G','A','S','Y','Q'],['A','S','A','D','B']]
# a=int(input())
# for i in range(len(arr)):
#     print(arr[i][a], end="")

# arr=[]
# lst=[0 for i in range(6)]
# for i in range(2):
#     arr.append([*map(int,input().split())])
# cnt=0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         lst[cnt]=arr[i][j]
#         cnt+=1
# lst.sort()
# cnt=0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         arr[i][j]=lst[cnt]
#         cnt+=1
# for i in range(len(arr)):
#     print(*arr[i])

# arr=[]
# arr.append([*map(int,input().split())])
# if len(arr[0])>=4:
#     arr[0].sort()
#     cnt=0
#     for i in range(2):
#         for j in range(3):
#             print(arr[0][cnt], end=" ")
#             cnt+=1
#         print()
# else:
#     lst=[0 for i in range(6)]
#     arr.append([*map(int, input().split())])
#     cnt=0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             lst[cnt]=arr[i][j]
#             cnt+=1
#     lst.sort()
#     cnt=0
#     for i in range(2):
#         for j in range(3):
#             print(lst[cnt], end=" ")
#             cnt+=1
#         print()

# lst=[0 for i in range(9)]

# print("c:\\python_project\\test")

# post=int(input("게시글의 총 갯수를 입력하세요:"))
# page=int(input("한 페이지에 필요한 게시글 수를 입력하세요:"))

# if post%page==0:
#     print(post//page)
# else:
#     print(post//page+1)

# person_1=input()
# person_2=input()
# print(f"{person_1}\n\n\n{person_2}")


# 실습 2

# a=int(input())
# b=int(input())

# result=(a//b+(bool(a%b)))
# print(result)

# sum=0
# for i in range(1,1000):
#     if i%2==0:
#         sum+=i
#     else:
#         if i%7==0:
#             sum+=i
# print(sum)

# score = {
#     'python': 80,
#     'django': 89,
#     'web': 83
# }
# score["algorithm"]=90
# score["python"]=85
# average=0
# for i in score:
#     average+=score[i]
# print(average/4)

# s = input('숫자를 입력해주세요 : ')
# sum=0
# for i in range(len(s)):
#     sum+=int(s[i])
# print(sum)

# lst=[0 for i in range(9)]
# for i in range(3):
#     a,b=[*map(int,input().split())]
#     for j in range(a,b+1):
#         lst[j]+=1
# print(*lst)

# a,b,c=[*map(int,input().split())]
# temp=a
# for i in range(c):
#     a=temp
#     for j in range(b):
#         print(a, end=" ")
#         a+=1
#     print()

# people={'A','B','C','Z','E','T','Q'}
# black=input()
# for i in range(len(black)):
#     cnt=0
#     for j in people:
#         if black[i]==j:
#             cnt+=1
#     if cnt==1:
#         print(f"{black[i]}=마을사람")
#     else:
#         print(f"{black[i]}=외부사람")

# moonjang=input()
# cnt=0
# for i in range(len(moonjang)-1):
#     if ord(moonjang[i])>=65 and ord(moonjang[i])<=90:
#         if ord(moonjang[i+1])>=97 and ord(moonjang[i+1])<=122:
#             cnt+=1
#     else:
#         if ord(moonjang[i+1])>=65 and ord(moonjang[i+1])<=90:
#             cnt+=1
# if cnt==len(moonjang)-1:
#     print("개구리문장")
# else:
#     print("일반문장")

# T=int(input())

# for i in range(T):
#     a,d,n=[*map(int,input().split())]
#     mul=1
#     for j in range(n):
#         mul*=a
#         a+=d
#     print(mul%(10*6+3))

# T=int(input())

# for i in range(T):
#     N,M=[*map(int,input().split())]
#     num=[*map(int,input().split())]
#     for j in range(M):
#         num.append(num[0])
#         del num[0]
#     print("#%d %d" %(i+1, num[0]))

s={1,2,3,4,5}
s.add(6)
print(s)
s.update([11,12,8,7,6])
print(s)

s.remove(6)
print(s)
s.discard(12)#값 없어도 버그 안남
print(s)
s.clear()
print(s)

# 집합
s1=[1,2,3,4,5]
s2=[2,4,6,8]

# 교집합
s1,s2=set(s1),set(s2)
print(s1&s2)

# 합집합
print(s1|s2)
print(s1.union(s2))

# 차집합
print(s1-s2)

# 좋은 코드...
# 질적인 측면 : 가독성이 좋은 코드(타인이 쉽게 이해할 수 있는 코드)
# 양적인 측면 : 메모리를 적게 사용하거나 실행했을 때 빠르게 처리가 되는 코드

# 변수명 함수이름 신경써서
# 코딩컨벤션

# a = 3
# b = 6
# c = -5
# # a*(x**2)+b*x+c=0
# x=(round((-b+(b**2-4*a*c)**(1/2))/2/a,3), round((-b-(b**2-4*a*c)**(1/2))/2/a,3))
# print(x)

# def inputt():
#     a=[*map(int,input().split())]
#     return a
# def calc(a):
#     sum=0
#     for i in range(len(a)):
#         sum+=a[i]
#     print(sum)
# calc(inputt())

# T=int(input())

# for i in range(T):
#     N=int(input())
#     lst=[3,5]
#     if N==20:
#         print("#%d %d" %(i+1,lst[0]))
#     elif N==30:
#         print("#%d %d" %(i+1, lst[1]))
#     else:
#         for j in range((N-30)//10):
#             lst.append(2*lst[j]+lst[j+1])
#         print("#%d %d" %(i+1, lst[len(lst)-1]))
    
# T=int(input())

# for i in range(T):
#     N=int(input())
#     lst=[*map(int,input().split())]
#     max1=lst[0]
#     min1=lst[0]
#     for j in range(N):
#         for k in range(j+1,N):
#             if max1<lst[k]:
#                 max1=lst[k]
#             if min1>lst[k]:
#                 min1=lst[k]
#     print("#%d %d" %(i+1, max1-min1))

T=int(input())

for i in range(T):
    K ,N, M=[*map(int,input().split())]
    charge=[*map(int,input().split())]
    bus_stop=[j for j in range(N+1)]
    charge.insert(0,0)
    charge.append(N)
    dis_check=0
    for j in range(len(charge)-1):
        if charge[j+1]-charge[j]>K:
            dis_check+=1
    if dis_check>0:
        print("#%d %d" %(i+1, 0))
    else:
        check_charge=0
        charge_dis=[]
        for j in range(len(charge)-1):
            charge_dis.append(charge[j+1]-charge[j])
        temp=charge_dis
        dis_sum=charge_dis[0]
        charge_check=0
        while len(charge_dis)!=0:
            if dis_sum<=K:
                dis_sum+=charge_dis[1]
            else:
                charge_check+=1
                cnt+=1
                del charge_dis[:cnt+1]
                dis_sum=charge_dis[0]
        print("#%d %d" %(i+1, charge_check))        
        # for j in range(len(temp)):
        #     dis_sum=0
        #     cnt=0
        #     while dis_sum<=K:
        #         dis_sum=charge_dis[0]
        #         for k in charge_dis:
        #             if dis_sum<=K:
        #                 cnt+=1
        #                 dis_sum+=k
        #     check_charge+=1
        #     del charge_dis[:cnt+1]
        #print("#%d %d" %(i+1, check_charge))
                        
            
            
