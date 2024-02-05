def main():
    user = shorten(input("Input: ").strip())
    print(f"Output: {user}")


def shorten(words):
    vowels_upper = ["A", "E", "I", "O", "U"]
    vowels_lower = ["a", "e", "i", "o", "u"]
    output_word = ""

    for word in words:
        if word not in vowels_lower and word not in vowels_upper:
            output_word += word
        else:
            continue
    return output_word


if __name__ == "__main__":
    main()
