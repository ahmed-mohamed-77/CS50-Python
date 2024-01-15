import random


def main():
    print("Welcome to the Little Professor Addition Calculator!")

    while True:
        level = get_level()
        x, y = generate_addition(level)

        try:
            user_answer = float(input(f"What is the answer to {x} + {y}? "))

            if check_addition(x, y, user_answer):
                print("Correct! Well done.")
            else:
                correct_answer = calculate_addition(x, y)
                print(f"Sorry, the correct answer is {correct_answer}. Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again != 'yes':
            print("Thank you for playing. Goodbye!")
            break


def get_level():
    return int(input("Enter the maximum number for the level: "))


def generate_addition(level):
    x = random.randint(1, level)
    y = random.randint(1, level)
    return x, y


def calculate_addition(x, y):
    return x + y


def check_addition(x, y, user_answer):
    return user_answer == calculate_addition(x, y)


if __name__ == "__main__":
    main()
