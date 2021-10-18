# python  built in functions

# a=3
# b=3
# c=sum((a,b))
# print(c)


# user defined function

#
# def function1():
#     print("This function has been called")
#
#
# function1()
#
# print(function1())
#


def funtion2(a,b):
    average=(a+b)/2
    return average

def funtion3(a,b):
    average=(a+b)/2
    print( average)


funtion2(56,6)
funtion3(56,6)
d=funtion2(3,5)
print(d)
e=funtion3(76,5)
print(e)



# very important concept here
# non-returning function- a funtion which doesn't have return statement so it doesn't return anything
# returning function- a function with a return statement which returns the output

# a returning function returns the output to a variable or it replaces the function with the output itself

# a= myfunction(d,e)        suppose this is a function call and it is assigned to the variable a
#  now a=3    where 3 is the value returned by the function after executing itself 




def average_num(a,b):

    """this is a docstring -a sentence or comment in first line of a function which describes about the function"""
    average=(a+b)/2
    return average


print(average_num.__doc__)
# this is a way to print docstring of a function, here we don't use parenthesis to print docstring


print(sum.__doc__)
# this is a docstring of built-in function


