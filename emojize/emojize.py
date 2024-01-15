import emoji

user = input("Input: ").strip()
print(emoji.emojize(f"Output: {user}", language="alias"))
