def main():
    result = Mass_energy_equivalence()
    formatted_result = "{:f}".format(result)
    print("E:", formatted_result)

def Mass_energy_equivalence():
    m = float(input("m: "))
    c = 300000000
    return m * (c ** 2)

main()
