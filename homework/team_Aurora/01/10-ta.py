initial_bites = int(input())
people_queue = []
while True:
    command = input()
    if command == "Start":
        break
    people_queue.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill"):
        _, beets = command.split()
        beets = int(beets)
        initial_bites += beets
    else:
        requested_bites = int(command)
        if initial_bites >= requested_bites:
            person_name = people_queue[0]
            print(f"{person_name} takes {requested_bites} bites")
            initial_bites -= requested_bites
            people_queue.pop(0)
        else:
            person_name = people_queue[0]
            print(f"{person_name} must wait")
            people_queue.pop(0)

print(f"{initial_bites} left")
