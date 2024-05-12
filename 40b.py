from random import randint


def solve_b40(As):
    mod_count = [0 for _ in range(100)]
    for a in As:
        mod_count[a % 100] += 1

    res = 0
    for x in range(1, 50):
        y = 100-x
        res += mod_count[x]*mod_count[y]

    # mod 50, mod 0 の場合の処理
    res += mod_count[50]*(mod_count[50]-1)//2
    res += mod_count[0]*(mod_count[0]-1)//2

    return res


def solve_b40_naive(As):
    N = len(As)

    res = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (As[i]+As[j]) % 100 == 0:
                res += 1

    return res


def test():
    assert (
        # solve_b40([10, 20, 30, 40, 50, 60, 70, 80, 90])
        solve_b40_naive([10, 20, 30, 40, 50, 60, 70, 80, 90])
        ==
        4
    )

    assert (
        solve_b40(
            [100, 100, 93, 100, 64, 80, 83, 30, 12, 51]
        )
        ==
        3
    )

    # Fuzzing test
    for _ in range(100):
        N = 1000
        As = [randint(1, 10**5) for _ in range(N)]
        r1 = solve_b40(As)
        r2 = solve_b40_naive(As)
        if r1 != r2:
            print(As)
            print(r1, r2)


def main():
    _ = input()
    A = list(map(int, input().split()))

    print(solve_b40(A))


# test()
main()
