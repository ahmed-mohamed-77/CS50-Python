import sys
import csv


def main():
    check_commandline_argument()

    output = []
    try:
        with open(sys.argv[1], "r") as file_reader:

            reader = csv.DictReader(file_reader)

            for row in reader:
                last_name, first_name = row["name"].split(",")
                output.append(
                    {
                        "first": first_name.strip(),
                        "last": last_name.strip(),
                        "house": row["house"].strip(),
                    }
                )

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file_writer:
        writer = csv.DictWriter(file_writer, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})

        for row in output:
            writer.writerow(
                {"first": row["first"], "last": row["last"], "house": row["house"]}
            )


def check_commandline_argument():

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
