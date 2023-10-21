children = input().split()
n = int(input())

while len(children) > 1:

    index_to_remove = (n - 1) % len(children)
    
    print(f"Removed {children.pop(index_to_remove)}")
print(f"Winner is {children[0]}")
