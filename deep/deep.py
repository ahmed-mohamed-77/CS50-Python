def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    user_input = user_input.strip().lower()

    if (user_input == "42") or (user_input == "forty-two") or (user_input == "forty two"):
        print("Yes")
    else:
        print("NO")

if __name__ == "__main__":
    main()
