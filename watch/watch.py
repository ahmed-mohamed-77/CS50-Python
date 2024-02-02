import re


def main():
    print(parse(input("HTML: ")))


"""return youtube links only"""


def parse(s):
    # give pattern accepts any source in the embed source url
    pattern_one = r"<iframe.*?src=\"(https?://(?:www)?\.?\w+\.\w+(?:\.\w+)?/\w+(\/[a-zA-Z0-9?=-]+)?)\""
    if check := re.search(pattern_one, s):
        # check that the pattern has anything other than youtube return none
        youtube_search = re.search(
            r"<iframe.*?src=\"(https?://(?:www\.?)?youtube\.\w+(?:\.\w+)?/\w+(\/[a-zA-Z0-9?=-]+)?)\"",
            s,
        )
        if not youtube_search:
            return None
        # check that the pattern has only youtube
        else:
            search_part = f"https://youtu.be{check.group(2)}"
            return search_part


if __name__ == "__main__":
    main()
