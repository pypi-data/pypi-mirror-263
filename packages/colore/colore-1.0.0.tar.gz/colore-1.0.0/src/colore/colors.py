"""
 Functions to define a fistful of color names associated with their ANSI codes,
 to use them in a terminal
"""
import os

user_home = os.path.expanduser('~')

CUSTOM_ALIASES_PATHS = (user_home + "/.colore_aliases",
                        user_home + "/.config/colore_aliases")
COLOR_END = "\033[0m"
DEFAULT_COLOR = "\033[31m"

FG = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "lgrey": "37",
    "grey": "90",
    "lred": "91",
    "lgreen": "92",
    "lyellow": "93",
    "lblue": "94",
    "lmagenta": "95",
    "lcyan": "96",
    "white": "97",
}

BG = {
    "_black": "40",
    "_red": "41",
    "_green": "42",
    "_yellow": "43",
    "_blue": "44",
    "_magenta": "45",
    "_cyan": "46",
    "_lgrey": "37",
    "_grey": "100",
    "_lred": "101",
    "_lgreen": "102",
    "_lyellow": "103",
    "_lblue": "104",
    "_lmagenta": "105",
    "_lcyan": "106",
    "_white": "107",
}


def color_code(cc):
    return f"\033[{cc}m"


def basic_colors():
    fg = {x: color_code(y) for x, y in FG.items()}
    bg = {x: color_code(y) for x, y in BG.items()}
    return {**fg, **bg}


def custom_aliases():
    colors_dict = {}
    for path in CUSTOM_ALIASES_PATHS:
        if os.path.isfile(path):
            with open(path) as f:
                lines = [l for l in f.read().splitlines() if
                         len(l) > 0 and l[0] != "#"]
                for line in lines:
                    name, value = line.split(" ")
                    colors_dict[name] = color_code(value)
            break
    return colors_dict


def all_colors():
    basic = basic_colors()
    combined = {x[0] + y[0]: color_code(x[1] + ";" + y[1]) for x in FG.items()
                for y in BG.items()}
    custom = custom_aliases()
    return {**basic, **combined, **custom}
