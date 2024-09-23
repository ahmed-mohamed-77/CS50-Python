# target from this function is to return the time in decimal form
# like 7.5 ,  8.0 , 9.1
def convert(time: str) -> float:
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60
    # if it decimal value



def main():
    # Check the format is ver important
    user_input: str = input("What time is it format (HH:MM): ").strip()

    try:
        time: float = convert(time=user_input)

        """
        breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00,
        and dinner between 18:00 and 19:00.
        """
        if 7.0 <= time <= 8.0:
            print("breakfast time")
        elif 12.0 <= time <= 13.0:
            print("lunch time")
        elif 18.0 <= time <= 19.0:
            print("dinner time")
    except ValueError:
        print("Invalid time  Format".upper())


if __name__ == "__main__":
    main()
