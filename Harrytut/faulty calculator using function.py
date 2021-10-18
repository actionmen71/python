def summ(a, b):

    return a + b


def subb(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print("Chose the operation:")
operator_input = input(" 1. Addition 2. Subtraction 3. Multiplication 4.Division:")
first_input = int(input("Enter the first number:"))
second_input = int(input("Enter the second number:"))

if ((operator_input == "3" or operator_input == " Multiplication") and (first_input == 45 or first_input == 3) and (
        second_input == 45 or second_input == 3)):
    print("Output:555")
elif ((operator_input == "4" or operator_input == "Division") and (first_input == 56 or first_input == 6) and (
        second_input == 56 or second_input == 6)):
    print("Output:4")
elif ((operator_input == "1" or operator_input == "Addition") and (first_input == 56 or first_input == 9) and (
        second_input == 56 or second_input == 9)):
    print("Output:77")

elif (operator_input =="3" or operator_input == " Multiplication"):
    print("Output:", mul(first_input, second_input))

elif (operator_input == "4" or operator_input == " Division"):
    print("Output:", div(first_input, second_input))
elif (operator_input =="1" or operator_input == " Addition"):
    print("Output:", summ(first_input, second_input))

elif (operator_input == "2" or operator_input == " Subtraction"):

    print("Output:", subb(first_input, second_input))
