queue = []

while True:
    command = input()
    if command == "END":
        print(f"{len(queue)}people remaining.")
        break
    elif command == "PAID":
        for customer in queue:
            print(customer)
        queue.clear()
    else:
        queue.append(command)