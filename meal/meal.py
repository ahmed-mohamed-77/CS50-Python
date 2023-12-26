def main():
    time_str = input("Enter the time in 24-hour format (HH:MM): ")
    hour = convert(time_str)

    if 7.0 <= hour <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= hour <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= hour <= 19.0:
        print("It's dinner time!")

def convert(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60.0

if __name__ == "__main__":
    main()
