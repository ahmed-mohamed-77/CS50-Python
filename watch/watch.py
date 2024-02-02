import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"(?<=src=\")(https://(?:www)?\.?\w+\.\w+(?:\.\w+)?/\w+(?:/[a-zA-Z0-9?=-]+)?)\""
    checker = re.search(pattern, s)
    return checker.group(1)

if __name__ == "__main__":
    main()
