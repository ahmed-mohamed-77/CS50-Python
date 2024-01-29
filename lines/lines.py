import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as file:
            if not sys.argv[1].endswith(".py"):
                sys.exit("Not a Python file")

            count = 0
            for line in file:
                # Skip empty lines and lines starting with #
                if line.strip() == "" or line.strip().startswith("#"):
                    continue
                count += 1

            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
