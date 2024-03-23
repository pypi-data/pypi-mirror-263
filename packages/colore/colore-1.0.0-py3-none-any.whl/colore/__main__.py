import sys
from .filter import process
from .help import show_help


def main():
    if len(sys.argv) == 3 and (sys.argv[1] in ("-f", "--file")):
        process(sys.argv[2])
    elif len(sys.argv) == 2 and (sys.argv[1] in ("-h", "--help")):
        show_help()
    else:
        process()


if __name__ == "__main__":
    main()
