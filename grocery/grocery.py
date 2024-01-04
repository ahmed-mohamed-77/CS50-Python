
my_dict = {}
while True:
    try:
        item = input()

        # check if item is does exist in dictionary
        if item in my_dict:
          my_dict[item] += 1
        else:
          my_dict[item] = 1

    except EOFError:
        for i in sorted(my_dict.keys()):
            print(my_dict[i], i.upper())
        break
