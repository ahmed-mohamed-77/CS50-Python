# create empty dictionary
grocery = {}

# create infinite loop
while True:
    try:
        # get the user input
        item = input().strip().lower()
        
        if item in grocery:
          grocery["item"] += 1
        else:
          grocery["item"] = 1

    except EOFError:
        for key in sorted(grocery.keys()):
          print(key, grocery[key])
        break
