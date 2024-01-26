def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_length(s) and check_begin(s) and check_spec(s) and check_numbers(s):
        return True
    else:
        return False


def check_length(s):
    if not 2<= len(s) <= 6:
        return False
    else:
        return True

def check_begin(s):
    for c in s[:2]:
        if c.isdigit():
            return False
    return True


def check_spec(s):
    for c in s:
        if not c.isalpha() and not c.isdigit():
            return False
    return True

def check_numbers(s):
    firstnum = None
    for c in s:
        if c.isdigit():
            firstnum = c
            break
    if firstnum == None:
        return True
    if int(firstnum) == 0:
        return False
    index = s.index(firstnum)
    position = len(s) - index
    for c in s[-position:]:
        if not c.isdigit():
            return False
    return True


main()
