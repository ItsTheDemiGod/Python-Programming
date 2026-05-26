day = input("what day is it ? ")


match day : # what ever value u wanna match you write it here like in this case we are matching the day variable with the cases below
    
    case "monday":
        print("today is monday")

    case "tuesday":
        print("today is tuesday")
    case "wednesday":
        print("today is wednesday")
    case "thursday":
        print("today is thursday")
    case "friday":
        print("today is friday")
    case "saturday":
        print("today is saturday")
    case "sunday":
        print("today is sunday")
    case _:
        print("invalid day")
