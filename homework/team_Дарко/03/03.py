total_invites = int(input())
invites = set()
teachers_invites = []
other_invites = []

for _ in range(total_invites):
    code = input()
    invites.add(code)
    if code[0] in '0123456789':
        teachers_invites.append(code)
    else:
        other_invites.append(code)

arrived = 0
while True:
    guest = input()
    if guest == "END":
        break
    if guest in invites:
        invites.remove(guest)
        arrived += 1

print(len(invites))
for invite in teachers_invites:
    if invite in invites:
        print(invite)

for invite in other_invites:
    if invite in invites:
        print(invite)
