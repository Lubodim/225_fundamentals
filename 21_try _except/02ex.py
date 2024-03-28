def sum_list(lst):
    if len(lst) == 0:
        raise IndexError()
    if len(lst) == 1 and type(lst[0]) == str:
        raise Exception
    result = 0
    for el in lst:
        result += int(el)
    return result
my_list = input().split()
try:
    a = sum_list(my_list)
    print(a)
except IndexError:
    print("no numbers")
except ValueError:
    print("cant sum int and str")
except Exception:
    print("Invalid splits")
