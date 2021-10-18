# String formatting
# Ways to add variable to a string

a= "this is a variable named a and inside it is a string text "
b="another variable"
x=55

c=a+b
# c=x+b  this will not work
# first way to add two variables which is simple but very limited functionality
# cannot add x variable to c because x is integer so only limited to string
print(c)






# second way to add two string variables together


c="and this is first text"
t=55
d="this is second text %a " %t
# we can use s(string) and a after percent to add variable to string
# note that only one variable can be added this way and if we add more it generates error
# Here we can add integer variable to a string as we see after executing print statement below
print(d)


e="this is another example %s %s %s" %(t,c,d)
f="this is another example %s %s" %(c,t)
g="this is another example %s %s" %(c,t)
print(e)
print(f)
print(g)

# Here we can add definetly more than one varibales to a string variable with the help of tuples ()






# third way to add


# we will use dot format here

p="first text {1} {1}"
# above brackets determine the variable position when numbers are added they work like index
q=5
r=9
s= p.format(q,r)
t=p.format(r,q)
print(s)
print(t)


# finally the fstring way
# we can also perform calculation directly into f strings
u=f"fstring is here {q} {r} {4**6}"
print(u)


# fstring promotes structure and readability of string when adding variables