def fac(x):
    if x==0:
        return 1
    else:
        return x*fac(x-1)

y=1
while y==1:
    x=int(input("pick a number to check the factorial of "))
    print("the factorial of",x,fac(x))