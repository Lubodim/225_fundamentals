n = int(input())
parking_cars = set()
for _ in range(n):
    action, car_number = input().split(',')
    if action == "IN":
        parking_cars.add(car_number)
    elif action == "OUT":
        parking_cars.discard(car_number)
if parking_cars:
    print("\n".join(parking_cars))
else:
    print("Parking is emty!")
