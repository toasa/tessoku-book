def solve_b31(N):
    n_divisible_by_3 = N//3
    n_divisible_by_5 = N//5
    n_divisible_by_7 = N//7
    n_divisible_by_15 = N//15
    n_divisible_by_21 = N//21
    n_divisible_by_35 = N//35
    n_divisible_by_105 = N//105

    return (n_divisible_by_3 + n_divisible_by_5 + n_divisible_by_7)\
        - (n_divisible_by_15 + n_divisible_by_21 + n_divisible_by_35)\
        + n_divisible_by_105


def test():
    assert (solve_b31(10) == 6)
    assert (solve_b31(210) == 114)
    assert (solve_b31(100000000000) == 54285714286)


def main():
    N = int(input())
    print(solve_b31(N))


# test()
main()
