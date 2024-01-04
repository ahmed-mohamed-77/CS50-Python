import math
while True:
  try:
    #  percentage=(denominator / numerator)×100
    user_input = input("Fraction: ")
    numerator, denominator = map(int, user_input.split("/"))
    if numerator > denominator:
      raise ValueError

    result = round((numerator/denominator) * 100, 0)
    if result <= 1:
      print("E")
    elif result >= 99:
      print("F")
    else:
      print(f"{result}%")

    break
  except (ValueError, ZeroDivisionError):
    print()
    pass
