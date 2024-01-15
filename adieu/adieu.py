import inflect
p = inflect.engine()

names = []

while True:
    try:
      user = input("Name: ").strip()
      names.append(user)
    except EOFError:
      print()
      break

output = p.join(names)
print("Adieu, adieu, to", output)
