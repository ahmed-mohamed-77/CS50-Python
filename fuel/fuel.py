def main():
    while True:
      try:
          user = input("Fraction: ").strip()

          percentage = convert(user)
          gauge(percentage)

      except (ValueError, ZeroDivisionError):
          ...



def convert(fraction):
    number_one, number_two = map(int, fraction.split("/"))

    if number_one > number_two:
        raise ValueError

    result = round((number_one / number_two) * 100)
    return result



def gauge(percentage):
    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
