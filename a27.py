def gcd(a, b):
    if (a < b):
        a, b = b, a

    # a >= b を仮定
    while True:
        if b == 1:
            return 1
        if a % b == 0:
            return b
        a -= b

        if (a < b):
            a, b = b, a


def main():
    A, B = map(int, input().split())
    print(gcd(A, B))


main()
