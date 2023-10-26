stack = []

n = int(input())

for _ in range(n):
    command = input().split()
    action = int(command[0])
    if action == 1:
        stack.append(int(command[1]))
    elif action == 2:
        if not len(stack) == 0:
            stack.pop()
    elif action == 3:
        if not len(stack) == 0:
            print(max(stack))
    elif action == 4:
        if not len(stack) == 0:
            print(min(stack))
    elif action == 5:
        print(len(stack))

while not len(stack) == 0:
    print(stack.pop(), end=', ')
