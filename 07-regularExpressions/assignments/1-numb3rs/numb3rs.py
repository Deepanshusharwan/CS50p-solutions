
import sys
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_parts = ip.split(".")
    try:
        if len(ip_parts) != 4:
            return "False"
        for _ in ip_parts:
            if int(_) > 255 or int(_) < 0:
                return "False"
        return "True"

    except ValueError:
        return "False"


if __name__ == "__main__":
    main()
