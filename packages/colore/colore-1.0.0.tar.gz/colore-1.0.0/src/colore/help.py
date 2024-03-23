import sys

text_help = """
Highlight each input line that contains the PATTERN using COLOR.
Several pattern/color pairs can be indicated.

USE: colore [PATTERN1 COLOR1] [PATTERN2 COLOR2]...

Examples:
ls / | colore bin 31 var 33 lib "32;100"
ls / | colore bin red var yellow lib green_grey

PATTERNs can be any Python regular expression, including wildcards and special
characters. For example, you can use the wildcard `\d` or the class `[0-9]` to
indicate any number, the characters `^` and `$` to indicate the beginning and
end of a line respectively, etc.

COLORs can be defined using numerical ANSI codes (see man console_codes(4)).
For example, red text would be represented by the number `31`, green background
by the number `42`, and underline by the number `4`. Joining these three codes
with semicolons of the form `31;42;4` would obtain the code for underlined red
text on a green background.

The order is irrelevant. The semicolon `;` must be escaped with a slash `\`
(so the above example would be `31\;42\;4`), or the entire color code

COLOR can also be any of the following aliases:

Front colors:

black: 30
red: 31
green: 32
yellow: 33
blue: 34
magenta: 35
cyan: 36
lgrey: 37
grey: 90
lred: 91
lgreen: 92
lyellow: 93
lblue: 94
lmagenta: 95
lcyan: 96
white: 97

Baclkground colors:

_black: 40
_red: 41
_green: 42
_yellow: 43
_blue: 44
_magenta: 45
_cyan: 46
_lgrey: 37
_grey: 100
_lred: 101
_lgreen: 102
_lyellow: 103
_lblue: 104
_lmagenta: 105
_lcyan: 106
_white: 107

Combinations of foreground color and background color, such as withe_red or
lblue_blue, are also valid names.

If is specified a color name that does not exist and is not defined as an
alias, the color `31` (`red`) will be used.

Other Options:

-h, --help              show this help (if it is the only argument).

-f, --file FILEMANE     gets PATTERNS and COLORS from a file instead
                        of arguments.

The format of FILEMANE must be the following:

pattern
color
pattern_2
color_2
pattern_3
color_3

So each line containing a pattern must be followed by a line with the color
code or name that will be assigned to the lines containing that pattern.

For example:

data_[\d]*\.text
green
output\.log
blue_yellow
error\.log
grid
^[\d]?$
32;44

Custom color aliases:

Custom color names can be defined in one of the following files:

~/.colore_aliases
~/.config/colore_aliases

The color configuration file must consist of one line for each color.
Each line will begin with the alias for the color, followed by a space,
and the numbers that define the color separated by semicolons:

rojo_sub 31;1;4
verde 32
bold_underline 1;4

Blank lines or lines starting with the "#" character will be ignored.

User-created names take precedence over predefined names.
"""

def show_help():
    print(text_help)
