def check_names(p, name):
    result = []

    for n in name:
        result.append(p[n])
    return result

data = input().split()
name_list = input().split(", ")

person = {}
for i in range(0, len(data), 2):
    person[data[i]] = data[int(i) + 1]

try:
    a= check_names(person, name_list)
    print(*a, sep=", ")
except KeyError:
    print("This person does not exist in this dictionary")
else:
    print("That was ages of the persons")