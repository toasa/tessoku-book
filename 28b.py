
def solve_b28(n):
    MOD = 1000000007

    a1 = 1
    a2 = 1

    for i in range(3, n+1):
        a = a1+a2
        a %= MOD

        a1 = a2
        a2 = a

    return a


def test():
    assert (solve_b28(6) == 8)
    assert (solve_b28(8691200) == 922041576)


def main():
    n = int(input())
    print(solve_b28(n))


# test()
main()
