
vowels = [
    "a","e","i","o","u",
]
def main():
    word = input()
    print(shorten(word))


def shorten(word):
    output = ""
    for a in word:
        b = a.lower()
        if b in vowels:
            pass
        else:
            output += a
    return output


if __name__ == "__main__":
    main()
