import csv
import sys


def main():

    if len(sys.argv) == 3:
        try:
            with open(sys.argv[1],"r") as file , open(sys.argv[2],"w") as ofile:
                reader = csv.DictReader(file)
                writer = csv.DictWriter(ofile, fieldnames = ["first","last","house"])
                writer.writeheader()
                for row in reader:
                    name = row["name"].split(", ")

                    writer.writerow(
                        {
                            "first": name[0],
                            "last": name[1],
                            "house": row["house"]
                        }
                    )
        except FileNotFoundError:
            sys.exit("could not read the file")

    elif len(sys.argv) >3:
        sys.exit("Too many command-line arguments")

    else:
        sys.exit("Too few command-line arguments")



if __name__ == "__main__":
    main()
