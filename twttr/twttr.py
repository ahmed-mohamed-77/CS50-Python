user_input = input("Input: ").strip()
user_output = ""

for c in user_input:
    if c not in ["a", "e", "i", "o", "u"]:
        user_output += c

print(user_output, end="")
