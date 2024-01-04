while True:
    try:
        items = []
        item = input()
        items.append(item)

    except EOFError:
        print()
        pass
    else:
        for i in range(len(items)):
            print((i + 1), items[i])
