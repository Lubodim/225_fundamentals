from collections import deque

queue = deque()
# paid_customers = deque()

while True:
    command = input()

    if command == "END":
        break

    if command == "PAID":
        print(queue.popleft())
        # paid_customers.extend(queue)
        # queue.clear()
    else:
        queue.append(command)
#
# for customer in paid_customers:
#     print(customer)
print(f"{len(queue)} people remaining.")
