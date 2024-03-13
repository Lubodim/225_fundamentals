class Spridon(Exception):
    print("Mnogo mi e gotin Eksep6ana")
#
def something(n):
    # for i in range(n):
    #     if i == 2:
    #         raise Spridon("I o6te kak")
    #     if i == 5:
    #         raise ValueError("Invalid number")

    return "fun"

try:
    print(something(10))
except ValueError as ve:
    print("Mnogo losho - ", ve)
except Spridon as me:
    print("Towa e qko - ", me)
else:
    print("мина без грешка")
finally:
    print("Congratulations that is the result")







# def divide(a, b):
#     return int(a) / int(b)
#
# num1 = input()
# num2 = input()
# try:
#     print(divide(num1, num2))
# except ZeroDivisionError:
#     print("U can not divide by zero")
# except ValueError:
#     print("you must choose only numbers")
#

