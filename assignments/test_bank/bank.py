
def main():
    greetings = input("Greetings: ")
    print(f"${value(greetings)}")

def value(greetings):
    greetings = str(greetings.lower())
    if greetings.split('o')[0] == 'hell' or greetings.split()[0] == 'hello':
        value = 0
    elif greetings.split('h')[0] == '':
        value = 20
    else:
        value = 100
    return value

if __name__ == "__main__":
    main()
