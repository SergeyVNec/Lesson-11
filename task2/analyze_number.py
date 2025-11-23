days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

user_input = input("Enter a number from 1 to 7: ")

try:
    number = int(user_input)

    if 1 <= number <= 7:
        print("Day of the week:", days[number])
    else:
        print("There is no day of the week with this number.")
except ValueError:
    print("You entered non-numerical data.")
