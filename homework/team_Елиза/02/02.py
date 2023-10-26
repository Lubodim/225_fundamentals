#Това е функция, която приема поредица (sequence) като аргумент.
def reverse_sequence(sequence):
    #празен списък (stack), в който ще се съхраняват числата.
    stack = []
    #разделя поредицата на числа, използвайки split(", "),
    elements = sequence.split(", ")
    for element in elements:
        stack.append(element)
    #променлива, в която ще се съхранява обратната поредица, която ще бъде изградена.
    reversed_sequence = ""
    while stack:
        #В тялото на цикъла програмата взима последния елемент от стека
        reversed_sequence += stack.pop() + " "
    #Функцията връща обратната поредица, като използва .strip()
    return reversed_sequence.strip()


input_sequence = input("Enter number with , and interval: ")


reversed_result = reverse_sequence(input_sequence)
print("Reverse sequnce:", reversed_result)