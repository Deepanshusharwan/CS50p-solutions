
import sys
import csv
from tabulate import tabulate

def main():
    table =[]
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
            try:
                with open(sys.argv[1],"r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        table.append(row)
                    headers = "keys"
                    print(tabulate(table,headers,tablefmt = "grid"))

            except FileNotFoundError:
                sys.exit("No such file exists")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a python file")

    else:
        sys.exit("Too few arguments")


if __name__ == "__main__":
    main()
