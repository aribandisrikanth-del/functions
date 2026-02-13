try:
    n=int(input("pick a number "))
    u=int(input("pick another number "))
    r=n/u
    print(n,"divided by",u,"=",r)
except ZeroDivisionError:
    print("not divideble by zero")
except ValueError:
    print("you did not give a integer")
else:
    print("nothing happened")
finally:
    print("done")