bites = int(input())
queue = []
while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)
while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        _, beets = command.split()
        bites += int(beets)
    else:
        person_name = queue.popleft()
        requested_bites = int(command)
        if requested_bites <= bites:
            print(f"{person_name} takes {requested_bites} bites")
            bites -= requested_bites
        else:
            print(f"{person_name} must wait")

print(f"Leftover bites: {bites}")

