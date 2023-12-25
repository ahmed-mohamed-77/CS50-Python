def main():
    dollars = dollars_to_float()
    percent = percent_to_float()
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float():
    doller = float(input("How much was the meal? "))
    return doller

def percent_to_float():
    percentage = float(input("What percentage would you like to tip? ")) / 100
    return percentage

main()
