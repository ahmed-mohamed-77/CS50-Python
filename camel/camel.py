def main():
  user = input("camel case: ").strip()

  snack_case_convert(user)

def snack_case_convert(user_input):
    snack_case = ""
    for char in user_input:
      if char.isupper():
        snack_case +='_' + char.lower()
      else:
        snack_case += char
    print(snack_case)

if __name__ == "__main__":
  main()
