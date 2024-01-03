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
            for i in range(len(months)):
                if month_out == month[i]:
                    month = i + 1
            if "," in day_out:
                day_out = day_out.replace(",", "")
            if (1 <= month_position <= 12) and (1 <= int(day_out) <= 31):
                break
        except ValueError:
            # Print an error message if neither format matches
            print("Invalid date format. Please enter a valid date.")

# Print the formatted date
print(f"{year_out}-{month_out:02d}-{int(day_out):02d}")
