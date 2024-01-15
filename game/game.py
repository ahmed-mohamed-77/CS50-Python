import random

while True:
    try:
        # Get the level from the user (maximum number for the guessing range).
        user = int(input("Level: "))

        # Generate a random number within the specified level.
        generated_num = random.randint(1, user)

        # Check if the user's input is an integer (this condition is not needed).
        if isinstance(user, int):  # This condition is not needed as 'user' is already assigned an integer value.

            # Start a loop for the user to make guesses until they get it right.
            while True:
                # Prompt the user to make a guess.
                prompt = int(input("Guess: "))

                # Compare the user's guess with the generated number.
                if prompt > generated_num:
                    print("Too large!")
                elif prompt < generated_num:
                    print("Too small!")
                else:
                    # The user guessed the correct number.
                    print("Just right!")
                    break  # Exit the inner loop when the correct number is guessed.

            # Exit the outer loop after a correct guess is made.
            break

    except ValueError:
        # Handle the case where the user enters a non-integer value.
        # i am telling the program that i know about this error and ignoring it anyway
        pass
