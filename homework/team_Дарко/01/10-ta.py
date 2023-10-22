bites = int(input())
bites_taking = []
bites_waiting = []
people = []
while True:
    person = input()
    if person == 'Start':
        break
    else:
        people.append(person)
remaining_bites = bites
while True:
    bites_person = input().split(' ')
    if bites_person[0] == 'refill':
        refill_amount = int(bites_person[1])
        remaining_bites += refill_amount
    elif bites_person[0] == 'END':
        for person in bites_taking:
            print(f"{person} take bites")
        for person in bites_waiting:
            print(f"{person} must wait")
        print(f"{remaining_bites} bites left")
        break
    else:
        requested_bites = int(bites_person[0])
        if requested_bites <= remaining_bites:
            bites_taking.append(people.pop(0))
            remaining_bites -= requested_bites
        else:
            bites_waiting.append(people.pop(0))
