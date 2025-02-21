
import re
import sys


def main():
    print(count(input("Text: ")))


def count(text):
    pattern = r"\bum\b"
    match = re.findall(pattern,text,flags=re.IGNORECASE)
    if match:
        return len(match)

        return match.group()


if __name__ == "__main__":
    main()
