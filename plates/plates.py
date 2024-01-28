def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False


def is_valid(s):
    return check_length(s) and check_begin(s) and check_spec(s) and check_numbers(s)


def check_length(s):
    return 2 <= len(s) <= 6


def check_begin(s):
    return not any(c.isdigit() for c in s[:2])


def check_spec(s):
    return all(c.isalpha() or c.isdigit() for c in s)


def check_numbers(s):
    i = 0

    while i < len(plate_number) :

        if plate_number[i].isalpha() == False:
            if plate_number[i] == "0":
                return False
        i += 1


if __name__ == "__main__":
    main()
