import random
listre = [ "Mcd" , "domi" , "burgking"]
listmm = [ "Sandwitch" , "Smoothie" , "Icecream"]
listdm = [ "Cheese Pizza" , "Pineappel Pizza" , "Veggi Pizza"]
listbm = [ "Small burger" , "Large burger" , "Ex large burger"]
print(listre)
x = input("What resturant do you want the menue for: ")
if (x == "Mcd"):
    print("Here is the menu: ")
    print(listmm)
    y = random.randrange(0,len(listmm))
    print("I reccomend " + listmm[y])

if (x == "domi"):
    print("Here is the menu: " )
    print(listdm)
    y = random.randrange(0,len(listdm))
    print("I reccomend " + listdm[y])

if (x == "burgking"):
    print("Here is the menu: " )
    print(listbm)
    y = random.randrange(0,len(listbm))
    print("I reccomend " + listbm[y])
