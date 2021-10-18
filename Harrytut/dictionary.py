t={"harry":"burger","rohan":3,4:3,3:"3irty"}
# key can be string of number and value can also be string or number
print(t)
print(t["harry"])
# we can print value by giving key
t["abhi add kro"]=53
# we can add another key:value pair by using this method
print(t)
del t["abhi add kro"]
# to delete a key:value pair
print(t)




# to demonstrate copy function

# t1=t
# del t["harry"]
# print(t1)

# above syntax doesn't make truly a copy of t so if we make changes in t it will relect in t1

t1=t.copy()
del t["harry"]
print(t1)

# here we are making a copy of t in t1 so changes in t doesn't reflect in t1

print(t.keys())
print(t.items())
print(t.values())

