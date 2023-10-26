def count_shelves(clothes, shelf_capacity):
    shelves = 0
    current_sum = 0

    for cloth in clothes:
        current_sum += cloth
        if current_sum > shelf_capacity:
            shelves += 1
            current_sum = cloth

    if current_sum > 0:
        shelves += 1

    return shelves


clothes = map(int, input("Дрехи: ").split())
shelf_capacity = int(input("капацитет на рафта: "))

result = count_shelves(clothes, shelf_capacity)
print(result)