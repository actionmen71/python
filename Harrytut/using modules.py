import random
# Above module is builtin module so it is directly imported
import sklearn
# Above module is not a builtin module so it is need to be installed either by pip or some package installer



random_number= random.randint(1,100)
print(random_number)




romi= int(random.random()*100)
print(romi)





channels=["ftv","ctv", "star","hotstar"]
trphight= random.choice(channels)
print(trphight)