day = input("enter the number between (1-7): ")

match day :
    case "1":
        print("it is Monday")
    case "2":
        print("it is Tuesday")
    case "3":
        print("it is Wednesday")
    case "4":
        print("it is Thursday")
    case "5":
        print("it is Friday")
    case "6":
        print("it is Saturday")
    case "7":
        print("it is Sunday")
    case __:
        print("invalid input")