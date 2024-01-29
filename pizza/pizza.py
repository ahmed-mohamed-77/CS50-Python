import csv
import sys
import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    try:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")

        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            data = [line for line in reader]

        if data:
            header = data[0]
            table = tabulate.tabulate(data[1:],headers=header,tablefmt="grid")
            print(table)
        else:
            print("no data inside the table".title())
    except FileNotFoundError:
        sys.exit("File does not exist")
        
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
