# Dictionary for punctuation
punctuation = {"!", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "^", "]", "^", "_", "`", "{", ",", "|", "}", "~"}

# Main Function
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# "is_valid" Function
def is_valid(p):
    if len(p) < 2:
        return False
    elif len(p) > 6:
        return False
    elif contains_punctuation(p) == True:
        return False
    elif does_not_begin_with_letters(p) == True:
        return False
    elif zero_check(p) == False:
        return False
    elif number_check(p) == False:
        return False
    else:
        return True

# Checks if plate has any punctuation___COMPLETE
def contains_punctuation(x):
    for char in x:
        if char in punctuation:
            return True

# Checks if plate does not begin with 2 letters
def does_not_begin_with_letters (a):
    if a[0].isalpha() == False or a[1].isalpha() == False:
        return True

# Checks numbers: they must come at the end, not in the middle
## First number cannot be "0"
### AA1230 == Valid | AA12BB/AA12B3/AA0123 == Invalid
#### Check "0" first
def zero_check(z):
    i = 0
    while i < len(z):
        if z[i].isalpha() == False:
            if z[i] == "0":
                return False
            else:
                break
        i += 1

##### Check numbers second
def number_check(n):
    j = 0
    while j < len(n):
        if n[j].isnumeric() == True:
            if n[j + 1].isalpha() == False:
                return False
            else:
                break
        j += 1

# Run main function to complete
main()
