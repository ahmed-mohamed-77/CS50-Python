def main():
    # get user input
    msg = input()
    # call the convert function
    result = convert(msg)
    # print the result
    print(result)

def convert(msg):
    # convert :) to happy emoji
    msg1 = msg.replace(":)", "🙂")
    # convert :) to sad emoji
    msg2 = msg1.replace(":(", "🙁")
    return msg2

main()


