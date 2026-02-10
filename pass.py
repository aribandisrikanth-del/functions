n=int(input("pick a number preferably above 20 "))

if n%20==0:
    print("twist")
if n%15==0:
    pass
if n%5==0:
    print("fizz")
if n%3==0:
    print("buzz")

print("twist= divisible by 20")
print("  = divisible by 15 or by none of the above or below")
print("fizz= divisible by 5")
print("buzz= divisible by 3")