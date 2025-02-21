import random
import sys


def main():
    while True:
        try:
            scope = int(input("Level: "))
            answer = random.randrange(1, scope, 1)
            if scope < 1:
                pass
            else:
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if guess < 1:
                            pass

                        elif guess == answer:
                            print("Just right!")
                            break

                        elif guess > answer:
                            print("Too large!")

                        elif guess < answer:
                            print("Too small!")

                    except ValueError:
                        pass
                sys.exit()
        except ValueError:
            pass


main()