import re


def main():
    s = input()
    print(re.sub("\s+", ",", s.strip()))


main()
