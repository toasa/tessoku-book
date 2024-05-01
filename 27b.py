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


def solve_b27(x, y):
    return x*y//gcd(x, y)


def test():
    assert (solve_b27(25, 30) == 150)
    assert (solve_b27(998244353, 998244853) == 996492287418565109)


def main():
    x, y = map(int, input().split())
    print(solve_b27(x, y))


# test()
main()
