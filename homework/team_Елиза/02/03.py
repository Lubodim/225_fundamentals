n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    operation = int(command[0])
    if operation == 1:
        number = int(command[1])
        stack.append(number)
    elif operation == 2:
        if stack:
            stack.pop()
    elif operation == 3:
        if stack:
            print(max(stack))
    elif operation == 4:
        if stack:
            print(min(stack))
    elif operation == 5:
        print (len(stack))