n = int(input("Enter the number of invitations: "))

inv = set()
for _ in range(n):
    code = input("Код: ")
    inv.add(code)

arr = set()

while True:
    guest = input("Код: ")
    if guest == "END":
        break
    arr.add(guest)

missing_guests = inv - arr

print(len(missing_guests))
for guest in missing_guests:
    print(guest)