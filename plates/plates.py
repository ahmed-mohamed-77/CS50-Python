def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate_number):
    # check for the  length palte_number
    # max == 6
    # min == 2
    if 2 > len(plate_number) > 6:
        return False

    if isinstance(int, plate_number[-1]) == True:
        return False

    if plate_number[0].isalpha() == False or  plate_number[1].isalpha() == False:
        return False
    i = 0

    while i < len(plate_number) :

        if plate_number[i].isalpha() == False:
            if plate_number[i] == "0":
                return False
            else:
                break
        i += 1

    for character in plate_number:
        if character in [".", " ", "!", "?"]:
            return False

    return True


if __name__ == "__main__":
    main()
