# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3 -2.5 3
my_tuple = tuple([float(digit) for digit in input().split(" ")])

my_dict = {}
for dg in my_tuple:
    if dg not in my_dict:
        my_dict[dg] = 0
    my_dict[dg] += 1
print(my_dict)
counter = 0
for k, v in my_dict.items():
    counter += 1
    result = f"{k} - {v} times"
    print(result)
    if counter == 2:
        break