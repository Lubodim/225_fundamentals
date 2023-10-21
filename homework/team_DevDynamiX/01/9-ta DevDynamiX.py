queue = []

while True:
    command = input()

    if command == "PAID":
        for person in queue:
            print(person)
        queue.clear()
    elif command == "END":
        remaining = len(queue)
        print(f"{remaining} people remaining.")
        break
    else:
        queue.append(command)