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
    if len(plate_number) < 2 or len(plate_number) 6:
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

    j = 0
    while j < len(n):
        if n[j].isnumeric() == True:
            if n[j + 1].isalpha() == False:
                return False
            else:
                break
        j += 1

    for character in plate_number:
        if character in [".", " ", "!", "?"]:
            return False

    return True


if __name__ == "__main__":
    main()
