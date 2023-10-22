from collections import deque

names = input().split()
n = int(input())

children = deque(names)

while len(children) > 1:
    children.rotate(-n)
    removed_child = children.pop()
    print(f"Removed {removed_child}")

print(f"Winner is {children.pop()}")
