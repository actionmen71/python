import math
p = int( input("Enter the no of participants"))
i=0

if (p<100 or p>200):
    print("Invalid input! try again!")

else:
    if (p % 2==0):

        group=(p/4)
        if (group % 2==0):
            print(group,"---> Pariticipants of group A")
            print(group,"---> Pariticipants of group B")
            print(group,"---> Pariticipants of group C")
            print(group,"---> Pariticipants of group D")
        else:
            group=math.floor(group)-1

            # group= math.floor( (p/4))-1
            print(group,"--->Pariticipants of group A")
            print(group,"--->Pariticipants of group B")
            print(group,"--->Pariticipants of group C")
            print(group,"--->Pariticipants of group D")
    else:
        remainder= p%4
        group= math.floor((p/4))
        print(group,"--->Pariticipants of group A")
        print(group,"--->Pariticipants of group B")
        print(group,"--->Pariticipants of group C")
        print(remainder+group,"--->Pariticipants of group D")


