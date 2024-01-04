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

            if (1 <= month <= 12) and (1 <= int(day) <= 31):
                break

        except ValueError:
            # Print an error message if neither format matches
            print()
            pass

# Print the formatted date
print(f"{year}-{int(month):02d}-{int(day):02d}")
