import re


def main():
    user_input = input("Hours: ")
    result = convert(user_input)
    print(result)


def convert(s):
    pattern = r"\s?([0-9:]+)\s([A-Z]+)\s(?:[a-z ]+)([0-9:]+)\s([A-Z]+)"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid input format.")

    morning_time, am, night_time, pm = match.groups()

    # morning
    if morning_time and am == "AM":
        morning_time = format_time(morning_time)
    else:
        morning_time = format_time(morning_time, add_12_hours=True)

    # night
    if night_time and pm == "PM":
        night_time = format_time(night_time, add_12_hours=True)
    else:
        night_time = format_time(night_time)

    return f"{morning_time} to {night_time}"


def format_time(time_str, add_12_hours=False):
    if ":" in time_str:
        hours, minutes = map(int, time_str.split(":"))

        if minutes >= 60:
            raise ValueError("check the correct time")

        if add_12_hours and hours < 12:
            hours += 12
        return f"{hours:02d}:{minutes:02d}"
    else:
        time_str = int(time_str)
        if add_12_hours and time_str < 12:
            time_str += 12
            return f"{time_str}:00"
        else:
            return f"{str(time_str).zfill(2)}:00"


if __name__ == "__main__":
    main()
