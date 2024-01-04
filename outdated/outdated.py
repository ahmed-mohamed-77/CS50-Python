months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    # Get the input date from the user
    outdated = input("Date: ")

    try:
        # Attempt to parse the input with slashes (MM/DD/YYYY format)
        month, day, year = map(int, outdated.split("/"))
        if (1 <= month <= 12) and (1 <= day <= 31):
            break
    except ValueError:
        try:
            # Attempt to parse the input with full month name (Month Day, Year format)
            old_month, old_day, year = outdated.split(" ")
            # Find the position of the month in the list
            for i in range(len(old_month)):
                if old_month == months[i]:
                    month = i + 1

            day = old_day.replace(",", "")

            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break

        except ValueError:
            # Print an error message if neither format matches
            print()
            pass

# Print the formatted date
print(f"{year}-{int(month):02d}-{int(day):02d}")


Date: December 80, 1980
Traceback (most recent call last):
  File "/home/ubuntu/CS50-Python/outdated/outdated.py", line 12, in <module>
    month, day, year = map(int, outdated.split("/"))
    ^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'December 80, 1980'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/ubuntu/CS50-Python/outdated/outdated.py", line 26, in <module>
    if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                 ^^^^^
NameError: name 'month' is not defined. Did you mean: 'months'?
