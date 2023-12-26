

def main():
    meal_time = input("Enter times in HH:MM\n").split()
    convert(meal_time)


def convert(time):
    for time in alltimes:
     hour, min = [int(i) for i in time.split(":")]

     if (7 >= hour <= 8) and (0 >= min <= 60):
        print("breakfast time")

if __name__ == "__main__":
    main()
