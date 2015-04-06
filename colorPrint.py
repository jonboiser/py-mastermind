from colorama import Fore, Back
def colorPrint(string, color):
    assert color.__len__() == 1, "Color code is a single character."
    assert color in 'roygbp', "Color code must be one of r, o, y, g, b, p."

    colorDict = {
        'r': lambda x: Fore.RED + x,
        'o': lambda x: Fore.RED + Back.YELLOW + x + Back.RESET,
        'y': lambda x: Fore.YELLOW + x,
        'g': lambda x: Fore.GREEN + x,
        'b': lambda x: Fore.BLUE + x,
        'p': lambda x: Fore.MAGENTA + x,
    }

    return colorDict[color](string) + Fore.RESET

def coloredCode(code):
    out = ""
    for c in code:
        out += colorPrint(c, c)
    return out

