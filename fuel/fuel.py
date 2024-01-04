import math
while True:
  try:
    #  percentage=(denominator / numerator)×100
    user_input = input("Fraction: ")
    numerator, denominator = map(int, user_input.split("/"))
    if numerator > denominator:
      raise ValueError
    if denominator <= 4:
      denominator = denominator
    else:
      raise ValueError

    print(f"%{math.floor((numerator/denominator) * 100)}")
    break
  except (ValueError, ZeroDivisionError):
    print()
    pass
