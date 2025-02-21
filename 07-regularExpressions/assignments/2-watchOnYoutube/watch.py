
import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    result = re.search(
        r'^<iframe(\s*?)src\s*="(http|https)://(www\.)?youtube\.com/embed/(.*?)"', html)
    if result is not None:
        result = result.group()
        output = re.search(r'(https|http)://(www\.)?youtube\.com.*[^"]', result)
        output = output.group()
        output = output.replace("www.", '')
        output = output.replace("/embed", "")
        output = output.replace('"', "")
        output = output.replace(".com", '')
        output = output.replace("b", ".b")
        if not "https" in output:
            output = output.replace("http", "https")

        return output
    else:
        return result


if __name__ == "__main__":
    main()
