import random
peoplelist = [ "your Mom" , "Aida" , "Ani" , "your friend" , "your Dad" , "your Brother"]
complist = [ "is rly smart" , "is rlyyy pretty" , "is soo nice"]
g = random.randrange(0 , len(peoplelist))
h = random.randrange(0 , len(complist))
print( peoplelist[g] + " " + complist[h])
