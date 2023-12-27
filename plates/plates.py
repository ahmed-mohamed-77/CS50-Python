def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate_number):
   # Check if linces less than 2 numbers
   if plate_number < 2:
       return False

    # check if linces greater 6 numbers and characters
   if plate_number > 6:
       return False

   



main()
