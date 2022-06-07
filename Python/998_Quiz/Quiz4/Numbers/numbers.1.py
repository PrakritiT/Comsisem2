mini = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
maxn = -9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
lis = [6,9,32,28,15,22,3,18]
i =0
for i in range(0,len(lis)):
    if(lis[i]<mini):
        mini = lis[i]
print (str(mini))
for i in range(0,len(lis)):
    if(lis[i]>maxn):
        maxn = lis[i]
print (str(maxn))

sumn = 0
var = 0
for i in range (0,len(lis)):
    sumn = sumn + lis[i]
    var = var +1
    varn = var
ans = sumn/var
print(str(ans))