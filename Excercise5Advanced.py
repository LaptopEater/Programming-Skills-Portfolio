dictionary = {
    "1": "31",
    "2": "28",
    "3":  "31",
    "4": "30",
    "5": "31",
    "6": "30",
    "7": "31",
    "8": "31",
    "9": "30",
    "10": "31",
    "11": "30",
    "12": "31",
}
#I've created a dictionary and a variable function.
var = (input("Enter your month number = "))
if int(var) > 12 or  int(var) < 0:
    print("INVALID NUMBER")
else:
    days = dictionary[var]
    if int(var) == 2:
        answer = input("Is it the leap year?, Yes or No ")
        answer = answer.lower()
        if answer == "yes":
            days = int(days) + 1
            

    print("The days in that month is: ", days)




