weather=str(input("is the season autum or summer "))
def weather_condition():
    if weather=="autum":
        print("the weather should be cold and leafy")
    elif weather=="spring":
        print("the weather should be warm with the flowers blooming")
    else:
        print("your weather statment was invalid")
print(weather_condition())