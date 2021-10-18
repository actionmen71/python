# set is created using set keyword
# by definition set only adds unique numbers or values
# check 4 only prints one time

abc = set([1,2,3,4,4])
# here we have put a list in set

print(abc)
print(type(abc))


# adding elements in set

abc.add(5)
print(abc)


# we can perform many set operations here like union, intersection and difference and many more.

newset= set({1,2,3,3,4})
oldset= set({1,2,7,88})
oper= newset.union(oldset)
print(oper)
opera=newset.intersection(oldset)
print(opera)
operas= newset.difference(oldset)
print(operas)

print(newset,oldset,oper,opera,operas)
print(len(newset))
# here repeated numbers in set are not counted in len function