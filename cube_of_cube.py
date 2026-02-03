def cube(x):
    return x*x*x
def divide(x):
    if x%3==0:
        return cube(x)

x=int(input("pick a number to cube "))

print(divide(x))