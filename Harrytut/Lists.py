grocery= ["Harpic","vimab","deor",45]
print(grocery)
gr=["har","par","bar"]
gb=[3,5,2,5,3,]
gs=(3,5,2,5,3,)
gbr={3,5,2,5,3,}
gbs=[3,5,2,5,3,]
print(type(grocery))
print(type(gr))
print(type(gb))
print(type(gbr))
print(type(gs))

print(grocery[2])
# print(grocery

#there are multiple list functions
#sort()     reverse()      indexing of list[1:3:3] or slice
# len(num)          max(num)          min(num)
#numbers.append(80) will add 80 to the list name numbers but it will add it to the last position

#numbers.reverse()

# instead of append we can use insert to add value in list in any position
#numbers.insert(2,3)     2 being the positin and 3 being the value
# numbers.remove(3)         will remove value 3 from the list
# numbers.pop()  will remove the last value from the list





# list are created with [] square brackets while tuples are created with () round brackets which are
# immutable
tp=(2,3,3)
print(tp)
print(type(tp))

tpi=(1,)
print(tpi)
# tp[1]=3




# common swapping technique vs python swapping
a=1
b=2
print(a,b)
# common
temp=a
a=b
b=temp
print(a,b)

c=3
d=4
print(c,d)
# python swapping
(c,d)=(d,c)
print(c,d)

