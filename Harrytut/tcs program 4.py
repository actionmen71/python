def getSum(n):
    s = 0

    while (n != 0):
        e = (n % 10)
        s = s + (e ** 3)
        n = n // 10

    return s


number = int(input("enter number:"))

if (number < 200 or number > 10000):
    print("Invalid input! Try again")
else:
    for i in range(200, number+1):
        number2=number


        num = int(getSum(i))

        if(number2 == num):
            print("Your output is:", num)
            break



    else:
        print("no number")








