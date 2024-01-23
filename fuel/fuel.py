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

    number_one, number_two = map(int, fraction.split("/"))

    if number_one > number_two:
        raise ValueError

    result = round((number_one / number_two) * 100)
    return result


if __name__ == "__main__":
    main()
