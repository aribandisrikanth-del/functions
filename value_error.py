try:
    i=int(input("pick your age "))
    if i<=0:
        raise ValueError
except ValueError:
    print("your age is not possible")