import random
import sys

def main():
    # Get the user's chosen level
    user = get_level()

    # Initialize the counter for correct answers
    counter = 0

    # Loop for 10 questions
    for i in range(10):
        try:
            # Generate random integers based on the user's level
            x, y = generate_integer(user)

            # Prompt the user for an answer
            user_answer = int(input(f"{x} + {y} = "))

            # Check if the user's answer is correct
            if user_answer == (x + y):
                counter += 1  # Increment counter for correct answers
            else:
                print("EEE")  # Print error message for incorrect answers

        except ValueError:
            pass  # Ignore ValueError (non-integer input)

    # Print the user's final score
    print(f"Score: {counter}")


def get_level():
    # Prompt the user for the desired level (1, 2, or 3)
    return int(input("Level: "))


def generate_integer(level):
    # Generate random integers based on the user's chosen level
    if level == 1:
        x = random.randint(0, 10)
        y = random.randint(1, 10)
    elif level == 2:
        x = random.randint(1, 100)
        y = random.randint(1, 100)
    elif level == 3:
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)



if __name__ == "__main__":
    main()
