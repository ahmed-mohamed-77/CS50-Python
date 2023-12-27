def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate_number):
    # Check if plate number has less than 2 or more than 6 characters
    if len(plate_number) < 2 or len(plate_number) > 6:
        return False

    # Check if plate number starts with at least two letters
    if not plate_number[:2].isalpha():
        return False




main()
