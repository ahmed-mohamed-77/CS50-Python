user_input = input("Input: ").strip()
user_output = ""
for c in user_input:
    if c not in ["A", "E", "I", "O", "U"]:
        user_output += char
    print(c, end="")
