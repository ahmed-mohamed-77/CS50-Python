months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    # Get the input date from the user
    outdated = input("Date: ")

    try:
        # Attempt to parse the input with slashes (MM/DD/YYYY format)
        month_out, day_out, year_out = map(int, outdated.split("/"))
        if (1 <= month_out <= 12) and (1 <= day_out <= 31):
            break
    except ValueError:
        try:
            # Attempt to parse the input with full month name (Month Day, Year format)
            month_out, day_out, year_out = outdated.split(" ")
            # Find the position of the month in the list
            month_position = months.index(month_out) + 1

            day_out = day_out.replace(",", "")

            if (1 <= month_position <= 12) and (1 <= int(day_out) <= 31):
                break

        except ValueError:
            # Print an error message if neither format matches
            print()
            pass
# Print the formatted date
print(f"{year_out}-{month_position:02d}-{int(day_out):02d}")
