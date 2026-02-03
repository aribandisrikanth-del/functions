def tip(tip_per,spend):
    return tip_per*spend+spend

spend=float(input("how much did you spend "))
tip_per=float(input("how much percent do you want to tip. EX:0.1, 0.2 "))

print(tip(tip_per,spend))