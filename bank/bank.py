# greeting from the teller
greeting = input("Greeting: ").capitalize()
# hello pays $0
if "Hello" in greeting:
    print("$0")
# any greeting starting with H pays $20
elif any(phrases in greeting for phrases in ["How you doing", "Hey", "How's it going"]):
    print("$20")
# any other greetings pays $100
else:
    print("$100")
