def main():
    # take the user input
    user_input = input("Item: ").strip().capitalize()

    # fruits with calories
    fruits = {
        "Apple" : 130, "Avocado" : 50, "Banana" : 110, "Cantaloupe" : 50,
        "Grapefruit" : 60, "Grapes" : 90, "honeydew Melon" : 50,
        "Kiwifruit" : 90, "Lemon" : 15, "Lime" : 20, "Nectarine" : 60,
        "Orange" : 80, "Peach" : 60, "Pear" : 100, "Pineapple" : 50,
        "Plims" : 70, "Strawberries" : 50, "Sweet Cherries" : 100,
        "Tangerine" : 50, "Watermelon" : 80
    }

    for fruit in fruits:
        if fruit == user_input:
            print(f"Calories: {fruits[fruit]}")


if __name__ == "__main__":
    main()
