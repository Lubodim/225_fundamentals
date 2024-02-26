# a = ['Спиридон', 'е', 'много', 'готин', 'пич', 'но', 'Стамат', 'му', 'е', 'гадже']
#
# for i, el in enumerate(a):
#     print(f"index is {i} element is {el}")


import math


def find_root_square(numbers):
    result_square_root = []
    for number in numbers:
        result_square_root.append(f"Square of {number} = {math.sqrt(number):.2f}")
    return result_square_root


num = list(map(int, input().split()))
gosho = find_root_square(num)
for i in gosho:
    print(i)


