import math


def isPrime(N):
    if N <= 3:
        return True

    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False

    return True


def solve_b26(N):
    res = []
    for i in range(2, N+1):
        if isPrime(i):
            res.append(i)

    return res


def test():
    assert (
        solve_b26(20)
        ==
        [2, 3, 5, 7, 11, 13, 17, 19]
    )


def main():
    N = int(input())

    res = solve_b26(N)
    for r in res:
        print(r)


# test()
main()
