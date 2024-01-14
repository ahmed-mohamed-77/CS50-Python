import sys
from pyfiglet import Figlet

def display_error(msg = "Invalid usage"):
    sys.exit(msg)

def figlet_font(name):
    user = input("Input: ")
    figlet = Figlet(font=name)
    print(figlet.renderText(user))

if __name__ == "__main__":
    try:
        fig = Figlet()
        fonts = list(fig.getFonts())
        ## test the program to accept only -f
        ## check the file name
        if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argc[1] == "--font"):
            font_name = sys.argv[2]
            if font_name in fonts:
                figlet_font(font_name)
            else:
                display_error()
        else:
            display_error()
    except Exception:
        display_error(Exception)
