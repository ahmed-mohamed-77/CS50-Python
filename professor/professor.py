import random
def main():
    # Get the user's chosen level
    user = get_level()
    # Loop for 10 questions
    score = simulate_game(user)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
    # Prompt the user for the desired level (1, 2, or 3)
            level =  int(input("Level: "))
            if 0 < level <= 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    # Generate random integers based on the user's chosen level
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def check_answer(x:int, y:int) :
    count_tries = 1
    while count_tries <= 3:
        try:
            # Prompt the user for an answer
            user_answer = int(input(f"{x} + {y} = "))
            # Check if the user's answer is correct
            if user_answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except ValueError:
            count_tries += 1
            print("EEE")

    print(f"{x} + {y} = {x + y}")
    return False

def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x,y =generate_integer(level)
        response = check_answer(x, y)
        if response == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()
