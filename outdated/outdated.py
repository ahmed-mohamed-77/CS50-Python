months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    # Get the input date from the user
    outdated = input("Date: ")

    try:
        day_out, month_out, year_out = map(int, outdated.split("/"))
        if (1 <= month_out <= 12) and (1 <= day_out <= 31):
            break
    except ValueError:
        try:
            day_out, month_out, year_out = outdated.split(" ")

            # to print the position month
            for num in range(len(months)):
                if month_out == months[num]:
                    month_position = num + 1

            day_out = day_out.replace(",", "")
            if (1 <= month_position <= 12) and (1 <= int(day_out) <= 31):
                break
        except ValueError:
            try:
                day_out, month_out, year_out = outdated.split(" ")

                # to print the position month
                for num in range(len(months)):
                    if month_out == months[num]:
                        month_position = num + 1

                day_out = day_out.replace(",", "")
                if (1 <= month_position <= 12) and (1 <= int(day_out) <= 31):
                    break
            except ValueError:
                print("Invalid date format. Please enter a valid date.")

print(f"{year_out}-{month_position:02d}-{int(day_out):02d}")
