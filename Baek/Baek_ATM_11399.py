N = int(input())
time = [*map(int, input().split())]

time = sorted(time)
time_sum = 0

for i, j in enumerate(range(N-1, -1, -1)):
    time_sum += time[i]*(j+1)

print(time_sum)

