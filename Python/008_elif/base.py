x = int(input("first integer: "))
y = int(input("second integer: "))
z = (input("operation(+,-,*,/): "))
if z == "+":
    a = x+y
    print(str(x) + "+" + str(y) + "=" + str(a))
elif z == "-":
    a = x-y
    print(str(x) + "-" + str(y) + "=" + str(a))
elif z == "*":
    a = x*y
    print(str(x) + "*" + str(y) + "=" + str(a))
elif z == "/":
    a = x/y
    print(str(x) + "*" + str(y) + "=" + str(a))
else:
    print("You did not select the right operation")
