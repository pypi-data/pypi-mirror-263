[Spanish version](https://bitbucket.org/psicobyte/colore/src/master/README.es.md)

# colore

![PyPI - Wheel](https://img.shields.io/pypi/wheel/colore)
![PyPI - License](https://img.shields.io/pypi/l/colore)
![PyPI - Downloads](https://img.shields.io/pypi/dw/colore)

Reads lines from `STDIN` and sends them to `STDOUT`; if any of those lines contain any of the regular expressions provided as arguments, it assigns a given text color and format using ANSI codes. Thus, lines containing different patterns can be displayed with different colors.

The color and format is always assigned to the entire line, even if the pattern only matches to part of it.

This program is designed to be used as a filter on the output of other commands.

## Usage:

```
colore [PATTERN COLOR] [PATTERN2 COLOR2] ...
```

Where `PATTERN`, `PATTERN2`... are regular expression patterns, and `COLOR`, `COLOR2`... are ANSI color codes or color names (see below).

For example:

```
cat file.log | colore ERROR 31 OK 32 WARNING "94;100"

cat file.log | colore ERROR red OK green WARNING lblue_grey

ls /var/log | colore "boot\.log\.[\d]+" 32\;41 "Xorg\.[\d]\.log" 33

ls /var/log | colore "boot\.log\.[\d]+" green_red "Xorg\.[\d]\.log" yellow
```

If a color code contains a semicolon `;`, it must be escaped with a forward slash `\` or by putting the entire code in quotes. Likewise, regular expressions that have special characters must be enclosed in quotes or have those characters escaped.

Instead of indicating the pattern and color pairs through arguments, they can be obtained from a text file, the path of which will be indicated as follows:

```
colore -f path/to/file
```

Or also:

```
coloer --file path/to/file
```

For example:

```
ps | colore -f patterns.txt
```

The format of this file must be the following:

```
pattern
color
pattern_2
color_2
pattern_3
color_3
```

So each line containing a pattern must be followed by a line with the color code or name that will be assigned to the lines containing that pattern.

For example:

```
data_[\d]*\.text
green
output\.log
blue_yellow
error\.log
grid
^[\d]?$
32;44
```

The `-f` or `--file` flag will only be interpreted as such if it is not accompanied by any arguments other than the file path. If there are more arguments, `-f` will be interpreted as a pattern (or a color name, depending on its position).

Likewise, the `-h` or `--help` flag will display help text only if it is the only argument.

Thus, the following arguments will not display the help, but will instead color the lines containing the text "--help" blue:

```
cat file.txt | colore --help blue
```

This is so that the strings `-h`, `--help`, `-f` or `--file` can be used as regular expressions.

## Install:

```
pip install colore
```

## Regular expressions

Any Python regular expression can be used, including wildcards and special characters. More information about regular expressions can be seen at [https://docs.python.org/3/howto/regex.html]

For example, you can use the wildcard `\d` or the class `[0-9]` to indicate any number, the characters `^` and `$` to indicate the beginning and end of a line respectively, etc.

If a `STDIN` line matches more than one pattern, the color corresponding to the first of those defined will be applied.

As already mentioned, regular expressions that have special characters that can be interpreted by the shell must be enclosed in quotes, or have those characters escaped with a forward slash `\`.

## Representation of colors and formats:

Colors and formats are encoded using numerical sequences as defined in the `console_codes(4)` man page, in its "Select Graphic Rendition" section, which is reproduced at the end of this document for convenience.

For example, red text would be represented by the number `31`, green background by the number `42`, and underline by the number `4`. Joining these three codes with semicolons of the form `31;42;4` would obtain the code for underlined red text on a green background. The order is irrelevant. The semicolon `;` must be escaped with a slash `\` (so the above example would be `31\;42\;4`), or the entire color code (in the mode `"31;42;4"`).

Some terminals may not support all or part of the colors or possible formats. Likewise, the exact representation of these colors and formats will depend on the specific terminal and its configuration.

More details can be seen on Wikipedia [https://en.wikipedia.org/wiki/ANSI_escape_code#SGR]

## Predefined color names:

Instead of numerical codes, a series of predefined names can be used to indicate the colors of both the text and the background:

### Front colors:

These aliases will assign the color they refer to text that matches the corresponding pattern:

* black
* red
* green
* yellow
* blue
* magenta
* cyan
* lgrey
* grey
* lred
* lgreen
* lyellow
* lblue
* lmagenta
* lcyan
* white

### Background colors:

These aliases are the same as the previous ones, but preceded by an underscore (_); They will not modify the color of the text, but rather the color of the background:

* _black
* _red
* _green
* _yellow
* _blue
* _magenta
* _cyan
* _lgrey
* _grey
* _lred
* _lgreen
* _lyellow
* _lblue
* _lmagenta
* _lcyan
* _white

Combinations of foreground color and background color, such as withe_red or lblue_blue, are also valid names.

If is specified a color name that does not exist and is not defined as an alias, the color `31` (`red`) will be used.

There are no predefined names for features such as underlining, italics, or blinking text, but nothing prevents aliases with those features from being added as seen in the next section.

## Custom color aliases:

Custom color names can be defined in one of the following files:

~/.colore_aliases
~/.config/colore_aliases

The color configuration file must consist of one line for each color. Each line will begin with the alias for the color, followed by a space, and the numbers that define the color separated by semicolons.

```
rojo_sub 31;1;4
verde 32
bold_underline 1;4
```

Blank lines or lines starting with the "#" character will be ignored.

User-created names take precedence over predefined names.

## Extract from the console_codes(4) manpage:

```
Select Graphic Rendition

       Several attributes can be set in the same sequence, separated by semicolons. An empty parameter
       (between semicolons or string initiator or terminator) is interpreted as a zero.
       param      result
       0          reset all attributes to their defaults
       1          set bold
       2          set half-bright (simulated with color on a color display)
       3          set italic (since Linux 2.6.22; simulated with color on a color display)
       4          set underscore (simulated with color on a color display) (the colors
                  used to simulate dim or underline are set using ESC ] ...)
       5          set blink
       7          set reverse video
       10         reset selected mapping, display control flag, and toggle meta flag
                  (ECMA-48 says "primary font").
       11         select null mapping, set display control flag, reset toggle meta flag
                  (ECMA-48 says "first alternate font").
       12         select null mapping, set display control flag, set toggle meta flag
                  (ECMA-48 says "second alternate font").  The toggle meta flag causes the
                  high bit of a byte to be toggled before the mapping table translation is
                  done.
       21         set underline; before Linux 4.17, this value set normal intensity (as is
                  done in many other terminals)
       22         set normal intensity
       23         italic off (since Linux 2.6.22)
       24         underline off
       25         blink off
       27         reverse video off
       30         set black foreground
       31         set red foreground
       32         set green foreground
       33         set brown foreground
       34         set blue foreground
       35         set magenta foreground
       36         set cyan foreground
       37         set white foreground
       38         256/24-bit foreground color follows, shoehorned into 16 basic colors
                  (before Linux 3.16: set underscore on, set default foreground color)
       39         set default foreground color (before Linux 3.16: set underscore off, set
                  default foreground color)
       40         set black background
       41         set red background
       42         set green background
       43         set brown background
       44         set blue background
       45         set magenta background
       46         set cyan background
       47         set white background
       48         256/24-bit background color follows, shoehorned into 8 basic colors
       49         set default background color
       90..97     set foreground to bright versions of 30..37
       100..107   set background, same as 40..47 (bright not supported)

       Commands 38 and 48 require further arguments:
       ;5;x       256 color: values 0..15 are IBGR (black, red, green,
                  ... white), 16..231 a 6x6x6 color cube, 232..255 a
                  grayscale ramp
       ;2;r;g;b   24-bit color, r/g/b components are in the range 0..255

```

