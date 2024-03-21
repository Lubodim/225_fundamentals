def input_to_inter(n):
    return int(n)

try:
    number = float(input())
    print(input_to_inter(number))
except ValueError:
    print("You can not make string to integer")