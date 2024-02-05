import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = (
        r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2["
        r"0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    )
    if ip_address := re.fullmatch(pattern, ip):
        ip_net_one, ip_net_two, ip_net_three, ip_net_host = map(
            int, ip_address.groups()
        )
        if (
            0 <= ip_net_one <= 255
            and 0 <= ip_net_two <= 255
            and 0 <= ip_net_three <= 255
            and 0 <= ip_net_host <= 255
        ):
            return True
        if (
            ip_net_one == 0
            and ip_net_two == 0
            and ip_net_three == 0
            and ip_net_host == 0
        ):
            return False
    else:
        return False


if __name__ == "__main__":
    main()


