# greeting from the teller
greeting = input("Greeting: ").capitalize()
# hello pays $0
if "Hello" in greeting:
    print("$0")
# any greeting starting with H pays $20
elif ["How you doing", "Hey", "How's it going"] in greeting:
    print("$20")
# elif "Hey"
# elif "How's it going"
# any other greetings
else:
    print("$100")
