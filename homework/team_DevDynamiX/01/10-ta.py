initial_bites = int(input())
queue = []

while True:
    command = input()

    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input()

    if command == "End":
        break
    elif command.startswith("refill "):
        refill_amount = int(command.split()[1])
        initial_bites += refill_amount
    else:
        person_name = queue[0]
        bites_requested = int(command)

        if bites_requested <= initial_bites:
            print(f"{person_name} take bites")
            initial_bites -= bites_requested
            queue.pop(0)
        else:
            print(f"{person_name} must wait")
            queue.pop(0)

print(f"{initial_bites} bites left")
