T = 10
for tc in range(1, T+1):
    leng, password = input().split()
    stack = []
    for i in range(int(leng)):
        if len(stack) == 0:
            stack.append(password[i])
        else:
            if stack[-1] == password[i]:
                stack.pop()
            else:
                stack.append(password[i])
    print(f'#{tc}', end=' ')
    print(*stack, sep='')