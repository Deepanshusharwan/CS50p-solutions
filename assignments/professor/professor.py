import random


def main():
    score = 0
    level = get_level()

    for i in range(10):
        mistakes = 0
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            try:
                if mistakes == 3:
                    print(f"{x} + {y} = {x+y}")
                    break

                answer = int(input(f"{x} + {y} = "))

                if answer == (x + y):
                    score += 1
                    break

                elif answer != (x+y):
                    print("EEE")
                    mistakes += 1

            except ValueError:
                print("EEE")
                mistakes += 1

    print(score)


def get_level():
    while True:
        feasible_levels = [1, 2, 3]
        try:
            level = int(input("Level: "))

            if level in feasible_levels:
                return level

            else:
                pass

        except ValueError:
            pass


def generate_integers(level):
    level -= 1
    score = 0
    for m in range(10):
        mistakes = 0
        a = random.randrange(10**level, (10**(level + 1)))
        b = random.randrange(10**level, (10**(level + 1)))

        while True:
            try:
                if mistakes == 3:
                    print(f"{a} + {b} = {a+b}")
                    break

                answer = int(input(f"{a} + {b} = "))

                if answer == a + b:
                    score += 1
                    break

                else:
                    print("EEE")
                    mistakes += 1

            except ValueError:
                print("EEE")
                mistakes += 1

    print(f"Score: {score}")


def generate_integer(level):
    level -= 1
    if level != 0:
        a = random.randrange(10**level, (10**(level + 1)))
        return a

    elif level == 0:
        a = random.randrange(0,10)
        return a


if __name__ == "__main__":
    main()
