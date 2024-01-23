# while True:
#     try:
#         # Get the user input as a fraction
#         user_input = input("Fraction: ")

#         # Split the input into numerator and denominator
#         numerator, denominator = map(int, user_input.split("/"))

#         # Check if the numerator is greater than the denominator
#         if numerator > denominator:
#             raise ValueError

#         # Calculate the percentage and round to the nearest integer
#         result = round((numerator / denominator) * 100)

#         # Evaluate the percentage and print the corresponding grade
#         if result <= 1:
#             print("E")
#         elif result >= 99:
#             print("F")
#         else:
#             print(f"{result}%")

#         break  # Exit the loop if input is valid

#     except (ValueError, ZeroDivisionError):
#         print()
#         pass  # Continue to the next iteration if an exception is caught

def main():
    while True:
      try:
          user = input("Fraction: ").strip()

          result = percentage(user)

          if result >= 99:
              print("F")
          elif result <= 1:
              print("E")
          else:
              print(f"{result}%")

          break
      except (ValueError, ZeroDivisionError):
          ...


def percentage(fraction):
    try:
        number_one, number_two = map(int, fraction.split("/"))

        if number_one > number_two:
            raise ValueError

        result = round((number_one / number_two) * 100)
        return result
    except (ValueError, ZeroDivisionError):
        ...


if __name__ == "__main__":
    main()
