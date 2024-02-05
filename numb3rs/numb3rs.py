import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = (
        r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2["
        r"0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    )
    if ip_address := re.search(pattern, ip):
        list_of_numbers = ip.split(".")
        for number in list_of_numbers:
            if 0 > int(number) > 255:
                return False
        if len(list_of_numbers) > 4:
            return False

        return True
    else:
        return False


if __name__ == "__main__":
    main()
