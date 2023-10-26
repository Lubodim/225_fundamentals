food_quantity = int(input())
orders = input().split()
orders = [int(order) for order in orders]


max_order = max(orders)


served = 0


for order in orders:
    if food_quantity >= order:
        food_quantity -= order
        served += 1
    else:
        break

print(max_order)

if served == len(orders):
    print("Orders complete")
else:
    remaining_orders = orders[served:]
    print("Оставащи поръчки:", ", ".join(map(str, remaining_orders)))
