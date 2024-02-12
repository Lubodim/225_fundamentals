class_members = input().split()

class_dict = {}
for el in range(0, len(class_members), 2):
    name = class_members[el]
    number = class_members[el + 1]
    if name not in class_dict.keys():
        class_dict[name] = int(number)


print(class_dict)

