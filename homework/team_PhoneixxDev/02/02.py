stack = []

n = int(input("Въведете брой команди: "))


def push_to_stack(num):
    stack.append(num)


def pop_from_stack():
    if stack:
        stack.pop()


def print_max_in_stack():
    if stack:
        print(max(stack))


def print_min_in_stack():
    if stack:
        print(min(stack))


def print_stack_length():
    print(len(stack))


for _ in range(n):
    command = input().split()
    operation = int(command[0])

    if operation == 1:
        num = int(command[1])
        push_to_stack(num)
    elif operation == 2:
        pop_from_stack()
    elif operation == 3:
        print_max_in_stack()
    elif operation == 4:
        print_min_in_stack()
    elif operation == 5:
        print_stack_length()

while stack:
    print(stack.pop(), end=" ")