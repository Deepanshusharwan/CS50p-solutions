def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
             continue

    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split('/')
    if x.isdigit() is False or y.isdigit() is False or int(x) > int(y):
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        tank = round(int(x) / int(y) * 100)
        return tank

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
