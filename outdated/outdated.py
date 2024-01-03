import datetime

# Get the input date from the user
outdated = input("Date: ")

# Check if the input date contains slashes (MM/DD/YYYY format)
if "/" in outdated:
    # If slashes are present, split the input using slashes
    month_out, day_out, year_out = map(int, outdated.split("/"))

    # Create a datetime object with the parsed values
    updated_date = datetime.datetime(year_out, month_out, day_out)

    # Print the formatted date
    print(updated_date.strftime("%Y-%m-%d"))

# If no slashes are present, assume the input date is in "Month Day, Year" format
else:
    # Parse the input date using strptime with the format "%B %d, %Y"
    input_date = datetime.datetime.strptime(outdated, "%B %d, %Y")

    # Print the formatted date
    print(input_date.strftime("%Y-%m-%d"))
