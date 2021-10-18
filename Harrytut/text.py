str="I am a good boy"



# print(str[0:5])# This is slicing of string
# print(len(str))
# print(str[0:15])
# print(str[0:])
# print(str[:0])
# print(str[:5])
# print(str[423:])
# print(str[5:])
# print(str[:])
# print(str[::2]) #Here slicing is done with gap value being 2
# print(str[::101]) # One thing to notice that whatever the gap
# value maybe it will definitely take the first character.
# Question  what is being taken by the compiler when 101 is placed 1 or 10 or 101.
# print(str[::])# Here slicing is done with gap value is default 1
# print(str[0:15:3]) #slicing with gap

# print(str[0:100])#So the upper limit doesn't create error
# print(str(0:3)) Hence, this doesn't work with round brackets only square brackets
# print(str{0:3})# Hence, this doesn't work with curly brackets only square brackets


# NEGATIVE INDICES

# print(str[-4:-2])
# print(str[-1:0:-1]) # negative gap in indice value reverses the string
print(str.endswith("boy"))
print(str.count("o"))
str1=print(str.lower())
str2="this is nice"
print(str2.capitalize())
print(str.upper())
print(str.replace("am","are"))