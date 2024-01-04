import datetime
# September 8, 1636 => %B%w%Y
# September 8 1636 => %B%w%Y
# 8 September 1636 => %B%w%Y
# 9/8/1636 => %-d%-m%Y
user_date = input("Date: ").strip()

# Define multiple format strings for parsing
formats = ["%B %d, %Y", "%B %d %Y", "%d %B %Y", "%m/%d/%Y", "%d/%m/%Y", "%B/%d/%Y"]
parse_date = None
for fmt in formats:
  try:
    parse_date = datetime.datetime.strptime(user_date, fmt).date()
    break # if parse is successful
  except ValueError:
    pass # continue trying other formats

if parse_date:
  unified_date = "%Y-%m-%d"
  formatted_date = parse_date.strftime(unified_date)
  print(formatted_date)

:( input of 23/6/1912 results in reprompt
    expected program to reject input, but it did not
:( input of 10 December, 1815 results in reprompt
    expected program to reject input, but it did not
:( input of October/9/1701 results in reprompt
    expected program to reject input, but it did not
:( input of 1/50/2000 results in reprompt
    expected program to reject input, but it did not
:( input of December 80, 1980 results in reprompt
    expected program to reject input, but it did not
:( input of September 8 1636 results in reprompt
    expected program to reject input, but it did not
