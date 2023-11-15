#зад 3 на PhoenixxDev
invitations = set()
arrived_guests = set()

n = int(input())
for _ in range(n):
    invitation = input()
    invitations.add(invitation)

while True:
    guest = input()
    if guest == "END":
        break
    arrived_guests.add(guest)

absentees = invitations.difference(arrived_guests)

print(len(absentees))
for guest in sorted(absentees):
    print(guest)