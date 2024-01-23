def main():
    while True:
        try:
            # Prompt the user for input
            user = input("Fraction: ").strip()

            # Convert the user input to percentage
            percentage = convert(user)

            # Display the result using the gauge function
            gauge(percentage)

            # Break out of the loop if no exception occurs
            break

        except (ValueError, ZeroDivisionError):
            # Handle invalid input, print error message, and continue the loop
            pass

def convert(fraction):
    # Convert the user input fraction to integers
    number_one, number_two = map(int, fraction.split("/"))

    # Check if the numerator is greater than the denominator
    if number_one > number_two:
        raise ValueError

    # Calculate the percentage and round it
    result = round((number_one / number_two) * 100)
    return result


def gauge(percentage):
    # Display the gauge result based on the calculated percentage
    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
