import random
wordlist = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        wordlist.append(l)
num = random.randrange(12972)
ans = wordlist[num]
print("In this game you will guess 6 5 letter words and hope it is the right one")
for i in range(0,6):
    guess = input("Pick a 5 letter word: ")
    if guess == ans:
        print("WOW YOU GUESSED RIGHT!")
        break
    else:
        print("Guess again")
    