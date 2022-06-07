x = int(input("line width: "))
l = int(input("Line length: "))
y = input("What character do you want the line to be?")

for b in range(0,x):
    print(" ")
    for a in range(0,l):
        print(y, end="")
