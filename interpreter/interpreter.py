def main():
    x,y,z = input("expression: "). split(" ")
    if y == "+":
        print(float(x) + float(z))
    if y == "-":
        print(float(x) - float(z))
    if y == "*":
        print(float(x) * float(z))
    if y == "/":
        print(float(x) / float(z))

if __name__ == "__main__":
    main()
