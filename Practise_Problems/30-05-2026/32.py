# Use match-case to simulate a simple traffic light: red, yellow, green → action message.

traffic_light = input("enter the traffic light colour ( red , yellow , green) :") 

match traffic_light :
    case "red" :
        print("STOP")
    case "yellow":
        print("slow down")
    case "green":
        print("GO")
    case __:
        print("invalid input")


