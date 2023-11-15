def parking_system(n):
    cars_in_parking = set()

    for _ in range(n):
        action, car_info = input().split(", ")
        car_number = car_info[3:]

        if action == "IN":
            cars_in_parking.add(car_number)
        elif action == "OUT":
            if car_number in cars_in_parking:
                cars_in_parking.remove(car_number)

    if cars_in_parking:
        for car in cars_in_parking:
            print(car)
    else:
        print("Parking is Empty")

n = int(input())
parking_system(n)
