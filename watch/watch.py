import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern_one = r"<iframe.*?src=\"(https?://(?:www)?\.?\w+\.\w+(?:\.\w+)?/\w+(\/[a-zA-Z0-9?=-]+)?)\""
    if check := re.search(pattern_one, s):
        youtube_search = re.search(r"<iframe.*?src=\"(https?://(?:www\.?)?youtube\.\w+(?:\.\w+)?/\w+(\/[a-zA-Z0-9?=-]+)?)\"",s)
        if not youtube_search:
            return None
        else:
            search_part = f"https://youtu.be{check.group(2)}"
            return search_part

if __name__ == "__main__":
    main()
