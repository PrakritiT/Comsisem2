x = input("What is your first and last name: ")
for i in range(0,len(x)):
    y = x[i:i+1]
    print(y)

for i in range(0,len(x)):
    y = x[i:i+1]
    s = " "
    if y == s:
        a = x[i: len(x)]
        b = x[0: i]
        print(a + " " + b)
        break