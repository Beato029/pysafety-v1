from Core.colors import *
from Components.get_version import *

def logo():
    
    logo1 = "┌─┐┬ ┬┌─┐┌─┐┌─┐┌─┐┌┬┐┬ ┬"
    logo2 = "├─┘└┬┘└─┐├─┤├┤ ├┤  │ └┬┘"
    logo3 = "┴   ┴ └─┘┴ ┴└  └─┘ ┴  ┴ "
    write = f"Welcome to PySafety\n{' ' * 5}Version: {get_version()[0] + " " + get_version()[1]}"
    line = "-" * (24 + 5 * 2)

    fade = [22, 28, 34, 40, 46, 82, 118, 82, 46, 40, 34, 28]

    def color_line(line, offset=0):
        colored = []
        for i, char in enumerate(line):
            color = fade[(i + offset) % len(fade)]
            colored.append(f'\033[38;5;{color}m{char}')
        return "".join(colored)

    print(" " * 5 + color_line(logo1, 0))
    print(" " * 5 + color_line(logo2, 4))
    print(" " * 5 + color_line(logo3, 8))
    print("")
    print(" " * 5 + color_line(write, 12))
    print(color_line(line, 16))
    print(RESET)