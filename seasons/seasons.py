from datetime import datetime, date
import inflect
import sys


def main():
    p = inflect.engine()
    age = input("Date of Birth: ").strip()

    try:
        user_age = datetime.strptime(age, "%Y-%m-%d").date()
        if not user_age:
            raise ValueError
    except ValueError:
        sys.exit("Invalid date")

    today_date = date.today()
    count_leapyear = count_leap_year(user_age.year, today_date.year)

    user_age_in_days = (today_date - user_age).days


    # count days in minutes
    user_age_in_minutes = user_age_in_days * 24 * 60


    convert_number_to_word = p.number_to_words(user_age_in_minutes, andword="")
    print(f"{convert_number_to_word.capitalize()} minutes")


def count_leap_year(start_date, end_date) -> int:
    count = 0
    for year in range(start_date, end_date+1):
        if is_leap_year(year):
            count += 1
    return count


def is_leap_year(year) -> bool:
    return (year % 4 == 0 and not year % 100 == 0) or (year % 100 == 0 and year % 400 == 0)


if __name__ == "__main__":
    main()
