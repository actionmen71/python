table=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

number=int(input("Enter the number:"))


def hexa(x):
    ab=x%16
    return ab


remainder=hexa(number)
if (remainder <=9 and remainder<0):
    print(remainder,"is hexa")
elif(remainder >9):
