def shutdown():
    ans=input("do you want to shutdown your computer ")
    if ans=="yes":
        return "shutting down computer"
    elif ans=="no":
        return "aborting shutdown"
    else:
        return "invalid input try again by restarting this program"
print((shutdown()))