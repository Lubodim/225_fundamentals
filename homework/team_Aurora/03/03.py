def party_invitations():
    n = int(input())
    invitations = set(input() for _ in range(n))

    arrivals = set()
    command = input()
    while command != "END":
        arrivals.add(command)
        command = input()

    missing_guests = invitations.difference(arrivals)

    print(len(missing_guests))
    for guest in sorted(missing_guests):
        print(guest)


party_invitations()
