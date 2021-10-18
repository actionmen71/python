# Here i will demostrate the use of try and exeption

try:
    a=int(input("enter the first no:"))
    b=int(input("enter the second no:"))

    print("everage:",(a+b)/2)
except Exception as g:
    print(g)

print("this line must execute and print itself")

# the error statement must come in the try section itself