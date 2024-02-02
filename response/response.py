import validator_collection

email = input("What's your email address? ").strip()
try:
    if checker := validator_collection.email(email):
        print("valid")
    else:
        print("invalid")
except validator_collection.errors.InvalidEmailError:
        print("invalid")
