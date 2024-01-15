import random
def main():
    while True:
        # Get the user's chosen level
        user = get_level()
        if 0 < user <= 3:
        # Loop for 10 questions
            for i in range(10):
                try:
                    # Generate random integers based on the user's level
                    x, y = generate_integer(user)

                    # Prompt the user for an answer
                    user_answer = int(input(f"{x} + {y} = "))

                    # Check if the user's answer is correct
                    if user_answer == (x + y):
                        counter = i + 1  # Increment counter for correct answers
                    else:
                        print("EEE")  # Print error message for incorrect answers
                except ValueError:
                    pass  # Ignore ValueError (non-integer input)
            if 0 < user <= 3:
                break
    # Print the user's final score
    print(f"Score: {counter}")


def get_level():
    # Prompt the user for the desired level (1, 2, or 3)
    return int(input("Level: "))


def generate_integer(level):
    # Generate random integers based on the user's chosen level
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 999)
        y = random.randint(10, 999)
    elif level == 3:
        x = random.randint(10, 999)
        y = random.randint(10, 999)
    return x, y



if __name__ == "__main__":
    main()
