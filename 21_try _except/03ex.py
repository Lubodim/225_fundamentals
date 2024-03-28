def integer(n):
    return int(n)

try:
    number = float(input())
    print(integer(number))
except ValueError:
    print("Cant make str to integer")