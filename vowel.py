x=input("type a word ")

for i in x:
    if i=="a" or i=="A" or i=="i" or i=="I"or i=="e" or i=="E"or i=="o" or i=="O"or i=="u" or i=="U":
        print("you typed a vowel")
        break
    else:
        print("not a vowel")