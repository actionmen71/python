dict1 = {"set": "a collection of well defined objects", "list": "an array of values", "port": "a computer address"}
print(dict1)
i = 0
while (i!=3):
    print("Enter a word to know its meaning: 1. set  2.list  3.port")
    x = input()
    print("Definition:")
    print(dict1.get(x))
    i += 1
