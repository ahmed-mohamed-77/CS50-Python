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
    shirt_file = Image.open(r"/home/ubuntu/CS50-Python/shirt/shirt.py")

    # get size of the shirt
    size = shirt_file.size

    # resize the muppet image
    muppet = image1.resize(size)

    # Shift the shirt upward by 20 pixels
    shift_up = 34
    paste_position = (0, -shift_up)

    # paste the shirt file
    muppet.paste(shirt_file, paste_position, shirt_file)

    # Convert the image to 'RGB' mode
    muppet = muppet.convert('RGB')

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
