from datetime import datetime
import inflect
import sys


def main():
    try:
        p = inflect.engine()
        age = input("Date of Birth: ").strip()
        user_age = datetime.strptime(age, "%Y-%m-%d").date()
        if not user_age:
            raise ValueError

        today_date = datetime.today().date()
        count_leapyear = count_leap_year(user_age.year, today_date.year)

        user_age_in_days = (today_date - user_age).days
        user_age_in_minutes = (user_age_in_days * 60) 
        convert_number_to_word = p.number_to_words(user_age_in_minutes)
        print(f"{convert_number_to_word} minutes")
    except ValueError:
        sys.exit("Invalid date")


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
