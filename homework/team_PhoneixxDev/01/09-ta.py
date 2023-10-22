queue = []

while True:
    name = input()
    if name == "END":
        print(f"{len(queue)} people remaining.")
        break

    elif name == "PAID":
        for customer in queue:
            print(customer)
        queue = []
    else:
        queue.append(name)