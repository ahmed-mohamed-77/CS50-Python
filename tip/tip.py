def main():
    dollars = dollars_to_float()
    percent = percent_to_float()
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float():
    dollar = input("How much was the meal? ")
    dollar = dollar.lstrip("$")
    return float(dollar)

def percent_to_float():
    percentage = input("What percentage would you like to tip? ")
    return percentage / 100

main()

