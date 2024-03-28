def divide(a, b):
    return int(a) / int(b)

while True:
    try:
        num1, num2 = input().split(", ")
    except NameError:
        print("U must split by (, )")
    except ValueError:
        print("U must have two numbers")
    try:
        print(divide(num1, num2))
    except ZeroDivisionError:
        print("You can not divide by ZERO")
    except ValueError:
        print("You can not divide by symbol")
    except NameError:
        print("I told you")