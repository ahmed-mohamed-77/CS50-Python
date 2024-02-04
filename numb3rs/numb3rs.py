import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip_address := re.search(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)(?:\.)?([0-9]+)?", ip):
        if len(ip_address.groups()) > 4:
            return False
        section_one, section_two, section_three, host = map(int, ip_address.groups())
        if section_one <= 255 and section_two <= 255 and section_three <= 255 and host <= 255:
            if section_one == 0 and section_two == 0 and section_three == 0 and host == 0:
                return False
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
