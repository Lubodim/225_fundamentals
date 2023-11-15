parked_cars = set()

n = int(input())

for _ in range(n):
    action, car = input().split(", ")

    if action == "IN":
        parked_cars.add(car)
    else:
        if car in parked_cars:
            parked_cars.remove(car)

if parked_cars:
    for car in parked_cars:
        print(car)
else:
    print("Parking is Empty")
