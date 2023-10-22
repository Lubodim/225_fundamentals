queue = []

while True:
    command = input()

    if command == "PAID":
        while queue:
            print(queue.pop(0))
        continue

    if command == "END":
        print(f"{len(queue)} people remaining.")
        break

    queue.append(command)
