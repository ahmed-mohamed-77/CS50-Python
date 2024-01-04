import datetime
# September 8, 1636 => %B%w%Y
# September 8 1636 => %B%w%Y
# 8 September 1636 => %B%w%Y
# 9/8/1636 => %-d%-m%Y
user_date = input("Date: ")

# Define multiple format strings for parsing
formats = ["%B %d, %Y", "%B %d %Y", "%d %B %Y", "%m/%d/%Y"]
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
