a = (input("What is your favorite number? Must use format('My favorite number is 69)': "))
print(a)
b = int(input("How old are you: "))
for i in range(0,len(a)):
    y = a[i:i+3]
    if y == "is ":
        x = a[len(a)-len(y)+1:len(a)]
z = int(x)*b
print("Your age times your favorite number is:" + str(z) +"")