import sys
import re


def main():
    if len(sys.argv) != 2:
        print("Invalid number of parameters")
        sys.exit(1)

    s = sys.argv[1]
    print(re.sub("\s+", ",", s.strip()))


main()
