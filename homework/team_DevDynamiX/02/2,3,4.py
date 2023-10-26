# Задача 2:
#
# stack = []
# n = int(input())
#
# for _ in range(n):
#     a = input().split()
#     command = int(a[0])
#
#     if command == 1:
#         number = int(a[1])
#         stack.append(number)
#     elif command == 2:
#         if stack:
#             stack.pop()
#     elif command == 3:
#         if stack:
#             print(max(stack))
#     elif command == 4:
#         if stack:
#             print(min(stack))
#     elif command == 5:
#         print(len(stack))
#
#
# for item in reversed(stack):
#     print(item, end=" ")
#
# Задача 3:

from collections import deque

food = int(input("Количество храна: "))
a = deque(map(int, input().split()))

print(max(a))

while a:
    if a[0] < food - a[0]:
        food -= a[0]
        a.popleft()
    else:
        break

if not a:
    print("Orders complete")
elif a != 0:
    print(f"Orders left {', '.join(map(str, a))}")

# Задача 4:
#
# a = map(int, input().split())
# b = int(input())
# shelves = 0
# current_shelf = 0
#
# for i in a:
#     if current_shelf + i <= b:
#         current_shelf += i
#     else:
#         shelves += 1
#         current_shelf = i
#
# if current_shelf > 0:
#     shelves += 1
#
# print(shelves)