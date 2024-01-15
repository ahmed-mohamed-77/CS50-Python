import sys
import requests
import json

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()

    # Use the data as a dictionary
    number_float = data["bpi"]["USD"]["rate_float"]
    if len(sys.argv) == 2:
        arg = float(sys.argv[1]) * number_float
        print(f"${arg:,.4f}")
    else:
      sys.exit("Missing command-line argument")

except requests.RequestException as e:
    print(f"Error fetching data: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except ValueError:
  sys.exit("Command-line argument is not a number")
