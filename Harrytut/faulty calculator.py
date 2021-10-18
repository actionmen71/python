try:
    print("Choose the following operation from the option:")
    operator_input = input(" 1. Addition 2. Subtraction 3. Multiplication 4.Division:")
    first_input = int(input("Enter the first number:"))
    second_input = int(input("Enter the second number:"))
    if (
            operator_input != "Addition" and operator_input != "1" and operator_input != "Subtraction" and operator_input != "2" and operator_input != "Multiplication" and operator_input != "3" and operator_input != "Division" and operator_input != "4"):
        print("Invalid input! try again!")
    else:
        if (operator_input == "Addition" or operator_input == "1"):
            if ((first_input == 56 and second_input == 9) or (first_input == 9 and second_input == 56)):
                print("Output: 77", )
            else:
                print("Output:", first_input + second_input)
        elif (operator_input == "Multiplication" or operator_input == "3"):
            if ((first_input == 45 and second_input == 3) or (first_input == 3 and second_input == 45)):
                print("Output: 555")
            else:
                print("Output:", first_input * second_input)
        elif (operator_input == "Division" or operator_input == "4"):
            if ((first_input == 56 and second_input == 6) or (first_input == 6 and second_input == 56)):
                print("Output: 4")
            else:
                print("Output:", first_input / second_input)
        elif (operator_input == "Subtraction" or operator_input == "2"):
            print("Output:", first_input - second_input)
except Exception as g:
    print(g)
