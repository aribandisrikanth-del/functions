x=input("type a word ")

for i in x:
    if i in "aAiIeEoOuU":
        print("you typed a vowel")
        break
    else:
        print(i,"is not a vowel")