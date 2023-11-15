n = int(input("Въведете броя на автомобилите: "))

s = set()

for _ in range(n):
    a, b = input("Въведете положението на автомобила и неговият номер: ").split(", ")

    if a == "IN":
        s.add(b)
    elif a == "OUT" and b in s:
        s.remove(b)

if s:
    for car in s:
        print(car)
else:
    print("Паркинга е празен")