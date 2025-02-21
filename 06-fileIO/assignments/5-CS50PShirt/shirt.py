
import sys
from PIL import Image
from PIL import ImageOps


def main():
    viable_extensions = [
        "jpeg", "jpg", "png",
    ]
    try:
        extension1 = sys.argv[1].split(".")[1]
        extension2 = sys.argv[2].split(".")[1]

    except IndexError:
        sys.exit("Please provide the input and output file name.")

    if len(sys.argv) == 3:
        if extension1 in viable_extensions and extension2 in viable_extensions and extension1 == extension2:
            try:
                with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as shirt:
                    img = ImageOps.fit(img, (600, 600))
                    img.paste(shirt, mask=shirt)
                    img.save(sys.argv[2])

            except FileNotFoundError:
                sys.exit("The file does not exist")

        else:
            sys.exit("give proper input")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
