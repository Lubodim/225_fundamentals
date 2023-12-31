from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    if food_quantity >= orders[0]:
        food_quantity -= orders[0]
        orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    remaining_orders = ', '.join(map(str, orders))
    print(f"Orders left: {remaining_orders}")
