def divide(a, b):
    return int(a) / int(b)

while True:
    try:
        num1, num2 = input().split(", ")
        print(divide(num1, num2))
    except ZeroDivisionError:
        print("You can not divide by ZERO")
    except ValueError:
        print("You can not divide by symbol")