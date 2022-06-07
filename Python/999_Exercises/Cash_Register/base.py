x = int(input("How many items do you wanna buy?"))
total = 0
thislista = []
thislistb = []
for b in range(0,x):
    a = input("What is the item name: ")
    y = float(input("How much did it cost: "))
    thislista.append(a)
    thislistb.append(y)
    total = total + y
for i in range(0,x):
    print(thislista[i] + "       " + str(thislistb[i]))
print("Your total is: " + str(total))
