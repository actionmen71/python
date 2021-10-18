import random

userpoints = 0

computepoint = 0

i = 1

while (i < 10):
    print("Round no:", i)

    list1 = ("Snake", "Gun", "Water")
    print("Choose your option: 1.Snake 2.Water 3.Gun")
    choices = input().capitalize()

    if(choices!= "Snake" and choices!= "Water" and choices!= "Gun"):
        print("Invalid input,try again! \n ")
        continue

    print("Your choice was:", choices)
    computechoices = random.choice(list1)
    print("Computer chose:",computechoices)
    i += 1
    if choices == computechoices:
        print("game tied:no points")
    elif(choices== "Snake" and computechoices== "Water"):
        userpoints += 1
        print("user won")
    elif choices == "Snake" and computechoices == "Gun":
        computepoint += 1
        print("computer won")
    elif(choices=="Water" and computechoices=="Gun"):
        userpoints += 1
        print("user won")
    elif(choices=="Water" and computechoices=="Snake"):
        computepoint += 1
        print("computer won")
    elif(choices=="Gun" and computechoices=="Snake"):
        userpoints += 1
        print("user won")
    elif(choices=="Gun" and computechoices=="Water"):
        computepoint += 1
        print("computer won")





print("Total score: User:", userpoints, " and Computer:", computepoint)

if ( userpoints > computepoint):
    print("Hurray! You 've won")
else:
    print("Sorry! You lose")
        
    


