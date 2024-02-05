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
    return  all(c.isalpha() for c in s[:2])


def check_spec(s):
    return all(c.isalpha() or c.isdigit() for c in s)


def check_numbers(s):
    firstnum = next((c for c in s if c.isdigit()), None)
    if firstnum is None:
        return True
    if int(firstnum) == 0:
        return False
    index = s.index(firstnum)
    position = len(s) - index
    return all(c.isdigit() for c in s[-position:])


if __name__ == "__main__":
    main()
