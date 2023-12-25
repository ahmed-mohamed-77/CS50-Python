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
    percentage = str(input("What percentage would you like to tip? "))
    percentage = percentage.rstrip("%")
    return float(percentage) / 100

main()

