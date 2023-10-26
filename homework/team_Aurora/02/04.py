def arrange_clothes(pile, capacity):
    shelves = 0
    current_shelf_capacity = capacity

    for clothes in pile:
        if clothes > current_shelf_capacity:
            shelves += 1
            current_shelf_capacity = capacity - clothes
        else:
            current_shelf_capacity -= clothes

    if current_shelf_capacity < capacity:
        shelves += 1

    return shelves

clothes_pile = list(map(int, input().split()))
shelf_capacity = int(input())

result = arrange_clothes(clothes_pile, shelf_capacity)
print(result)
