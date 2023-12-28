user_input = input("Input: ").strip()
user_output = ""
vowels_lower = ["a", "e", "i", "o", "u"]
vowels_upper = ["A", "E", "I", "O", "U"]

for c in user_input:
    if c not in vowels_lower and c not in vowels_upper:
        user_output += c

print(f"output: {user_output}")

