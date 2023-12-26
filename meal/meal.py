

def main():
    meal_time = input("Enter times in HH:MM\n").split()
    convert(meal_time)


def convert(time):

    hour, min = [int(i) for i in time.split(":")]

    if (7 >= hour <= 8) and (0 >= min <= 60):
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= time_in_hours <= 19.0:
        print("It's dinner time!")

if __name__ == "__main__":
    main()
