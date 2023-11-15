n=int(input())
invited_guest=set(map(str,range(1,n+1)))
arrived_guest=set()
while True:
    invitation=input()
    if invitation == "END":
        break
    arrived_guest.add(invitation)
not_attended={f"invited_guest-arrived_guest"}
if not_attended:
        not_attended = sorted(not_attended, key=lambda x: (not x.isdigit(), x))
        print(len(not_attended))
        print("\n".join(not_attended))
else:
        print("All guests attended the party")
