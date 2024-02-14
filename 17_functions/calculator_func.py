def add_func(num1, num2):
    return num1 + num2


def devide_func(num1, num2):
    if num2 == 0:
        return "Can not devide with zero"
    return num1 / num2


def myltiplay_func(num1, num2):
    return num1 * num2


def subtract_func(num1, num2):
    return num1 - num2


def main_func():
    while True:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the first number: "))
        operator = input("Choice between - + * / or Stop for end.: ")
        if operator == 'Stop':
            return
        if operator == '-':
            result = subtract_func(number1, number2)
        elif operator == '+':
            result = add_func(number1, number2)
        elif operator == '/':
            result = devide_func(number1, number2)
        elif operator == '*':
            result = myltiplay_func(number1, number2)
        else:
            continue
        print(result)
        return main_func()


main_func()

