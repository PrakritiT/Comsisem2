x = int(input("How long do you want the line to be?"))
y = input("Enter H for a horozantal line and V for a vertical line:")


if y == "H":
    for a in range(0,x):
        print("*", end="")
elif y == "V":
    for a in range(0,x):
        print("*")