from collections import deque

food_quantity = int(input("количество храна: "))

orders = deque(map(int, input().split()))

max_order = max(orders)

while orders:
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        break

if not orders:
    print(max_order)
    print("Orders complete")
else:
    remaining_orders = ", ".join(map(str, orders))
    print(max_order)
    print(f"Remaining orders: {remaining_orders}")
