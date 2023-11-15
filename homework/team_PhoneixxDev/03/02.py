#зад 2 на PhoenixxDev
n = int(input())
cars = set()

for _ in range(n):
    operation, car_number = input().split(', ')

    if operation == "IN":
        cars.add(car_number)
    elif operation == "OUT":
        cars.discard(car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking lot is empty")
