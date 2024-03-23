"""
 Filters stdin, coloring the lines containing the indicated pattern with its
 associated color
"""
import re
import sys

from .colors import COLOR_END, DEFAULT_COLOR, all_colors, color_code


def from_args():
    return get_pairs(sys.argv[1:])


def from_file(path):
    try:
        with open(path) as f:
            pairs = f.read().splitlines()
    except OSError as e:
        print(e)
        sys.exit()
    return get_pairs(pairs)


def get_pairs(pairs):
    pattern_color_code = re.compile("^[\d;]*$")
    colors_dict = all_colors()
    patterns = []
    colors = []
    for i in range(0, len(pairs), 2):
        try:
            compiled = re.compile(pairs[i])
        except re.error as e:
            print(e)
            sys.exit()
        patterns.append(compiled)
        if pattern_color_code.search(pairs[i + 1]):
            colors.append(color_code(pairs[i + 1]))
        else:
            colors.append(colors_dict.get(pairs[i + 1], DEFAULT_COLOR))
    return patterns, colors


def filter_lines(pairs):
    patterns, colors = pairs
    end_line = COLOR_END + "\n"
    for line in sys.stdin:
        for i in range(len(patterns)):
            if patterns[i].search(line):
                line = colors[i] + line.rstrip("\n") + end_line
                break
        print(line, end="")


def process(path=None):
    pairs = from_file(path) if path else from_args()
    filter_lines(pairs)
