from PIL import Image, ImageOps
import sys
from os.path import splitext


def main():
    check_commandline_argument()
    try:
        image1 = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # open shirt
    shirt_file = Image.open("shirt.png")

    # get size of the shirt
    size = shirt_file.size

    # resize the muppet image
    muppet = ImageOps.fit(image1, size)

    # paste the shirt file
    muppet.paste(shirt_file,  shirt_file)

    # create output muppet
    muppet.save(sys.argv[2])


def check_commandline_argument():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])[1].lower()
    file2 = splitext(sys.argv[2])[1].lower()

    image_ending = [".jpg",".jpeg",".png"]

    if file1 not in image_ending or file2 not in image_ending:
        sys.exit("Invalid output")
    elif file1 != file2:
        sys.exit("Input and output have different extensions")




if __name__ == "__main__":
    main()
