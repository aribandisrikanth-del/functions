while 1==1:
    def calculate(x,y):
        if c=="addition":
            return x+y
        elif c=="subtraction":
            return x-y
        elif c=="multiplication":
            return x*y
        elif c=="division":
            return x/y
        else:
            return "invalid mathmatical opperation"

    c=str(input("please select a mathmatical opperation addition,subtraction,mutiplication or division(if you type break it stops the code) "))
    if c=="break":
        break
    x=int(input("please select a number to "))
    y=int(input("please select a number to "))

    print(x,c,y,"=",calculate(x,y))