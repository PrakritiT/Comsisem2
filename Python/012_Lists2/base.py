import random
x = int(input("How many random numbers do you want me to generate? "))
thislist = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
y = (random.randrange(x))
for i in range (0,x):
    y = (random.randrange(len(thislist)))
    print(thislist[y], end=",")
    