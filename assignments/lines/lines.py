import sys

def main():
    n = 0
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1],"r") as file:
                lines = file.readlines()

                for line in lines:
                    line = line.strip()
                    if not line.startswith("#") and line != "":
                        n += 1
                print(n)
        except FileNotFoundError:
            sys.exit("No such file exists")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

    else:
        sys.exit("Too few arguments")

if __name__ == "__main__":
    main()
