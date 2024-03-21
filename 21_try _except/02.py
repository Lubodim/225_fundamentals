class Gosho(Exception):
    pass

def sum_func(lst):
    if not lst:
        raise IndexError
    if len(lst) == 1 and type(lst[0]) == str:
        raise Gosho
    result = 0
    for el in lst:
        result += int(el)
    return result
my_list = input().split()
try:
    print(sum_func(my_list))
except Gosho:
    print("Wrong number splits!")
except ValueError:
    print("You can not sum int and str!")
except IndexError:
    print("You can not sum empty list!")

