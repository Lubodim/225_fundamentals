start_qt = int(input())
data = input()
people = []
while data != 'Start':
    people.append(data)
    data = input()
data = input().split()

while data[0] != 'End':
    if data[0] == 'refill':
        start_qt += int(data[1])

    else:
        if int(data[0]) <= start_qt:
            print(people[0], 'takes bites')
            people.remove(people[0])
            start_qt -= int(data[0])
        else:
            print(people[0], 'must wait')
            people.remove(people[0])

    data = input().split()
print(f"Left {start_qt}")
