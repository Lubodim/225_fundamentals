clothes = list(map(int, input().split()))
capacity = int(input())
shelves = []

for cloth in clothes:
    if not shelves:
        shelves.append(cloth)
    else:
        current_shelf = shelves.pop()
        if current_shelf + cloth <= capacity:
            shelves.append(current_shelf + cloth)
        else:
            shelves.append(current_shelf)
            shelves.append(cloth)

print(len(shelves))
