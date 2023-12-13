input_var = input("enter a sentence: ")
input_var = input_var.capitalize()

if "Hello :)" in input_var:
    print("Hello 🙂")
elif "Goodbye :(" in input_var:
    print("Goodbye 🙁")
elif "Hello :)" in input_var and " Goodbye :(" in input_var:
    print("Hello 🙂 Goodbye 🙁")
