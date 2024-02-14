
def sum_func(a, b):
    return a + b


def even_func(my_list):
    even_list = []
    for num in my_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


number = list(map(int, input().split(", ")))
a = even_func(number)

if a:
    print(a)


print(sum_func(number))
