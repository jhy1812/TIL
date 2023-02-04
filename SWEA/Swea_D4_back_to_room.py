# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     student_room = []
#     for i in range(N):
#         student_room += [[*map(int, input().split())]]
#     for i in range(N):
#         if student_room[i][0]%2 == 1:
#             student_room[i][0] = (student_room[i][0]+1)//2
#         else:
#             student_room[i][0] = student_room[i][0]//2
#         if student_room[i][1]%2 == 1:
#             student_room[i][1] = (student_room[i][1]+1)//2
#         else:
#             student_room[i][1] = student_room[i][1]//2
#         if student_room[i][1] < student_room[i][0]:
#             student_room[i][0], student_room[i][1] =  student_room[i][1], student_room[i][0]

#         time = [0]*201
#         for i in range(N):
#             time[student_room[i][0]:student_room[i][1]] +=1

time = [1,2,3,5,4,5,6,3]

print(time[2:5])


    # time = 0

    # while len(student_room) != 0:
    #     time += 1
    #     check = student_room[0]
    #     del student_room[0]
    #     leng = len(student_room)
    #     for i in range(leng):
    #         if student_room[i][0] > check[1] or student_room[i][1] < check[0]:
    #             del student_room[i]
    # print(f'#{tc} {time}')

    # cnt = 0
    # check = 0

    # while cnt != N:
    #     time += 1
    #     cnt += 1
    #     for i in range(N-1, check-1, -1):
    #         if student_room[check][0] > student_room[i][1] or student_room[check][1] < student_room[i][0]:
    #             cnt += 1
    #         else:
    #             temp = i
    #     check = temp
    # print(f'#{tc} {time}')
                

