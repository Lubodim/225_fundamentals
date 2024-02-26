vehicles = input().split('>>')

tax = 0
tp_vehicle = None
years = 0
kilo = 0
total_tax = 0

for index in vehicles:
    tp_vehicle, years, kilo = index.split()
    if tp_vehicle == 'family':
        tax = 50
        years = int(years)
        kilo = int(kilo)
        tax -= years * 5
        tax += int(kilo / 3000) * 12

    elif current_index[0] == 'heavyDuty':
        tax = 80
        years = int(current_index[1])
        kilo = int(current_index[2])
        tp_vehicle = current_index[0]

        if tp_vehicle == 'heavyDuty':
            tax -= years * 8
            tax += int(kilo / 9000) * 14
            total_tax += tax
            print(f'A {tp_vehicle} car will pay {tax:.2f} euros in taxes.')

    elif current_index[0] == 'sports':
        tax = 100
        years = int(current_index[1])
        kilo = int(current_index[2])
        tp_vehicle = current_index[0]

        if tp_vehicle == 'sports':
            tax -= years * 9
            tax += int(kilo / 2000) * 18
            total_tax += tax
            print(f'A {tp_vehicle} car will pay {tax:.2f} euros in taxes.')

    else:
        print('Invalid car type.')

print(f'The National Revenue Agency will collect {total_tax:.2f} euros in taxes.')