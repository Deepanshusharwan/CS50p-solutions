def main():
    message = input('')
    print(convert(message))


def convert(text):
    text = text.replace(":)", '🙂')
    text = text.replace(':(','🙁')
    return text


main()
