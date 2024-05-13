def solve_b41(X, Y):
    res = []
    while (X, Y) != (1, 1):
        res.append((X, Y))
        if X < Y:
            Y -= X
        else:
            X -= Y

    res.reverse()

    return res


def test():
    assert (
        solve_b41(1, 1)
        ==
        []
    )

    assert (
        solve_b41(5, 2)
        ==
        [
            (1, 2),
            (3, 2),
            (5, 2),
        ]
    )


def main():
    X, Y = map(int, input().split())

    res = solve_b41(X, Y)

    print(len(res))
    for r in res:
        print("{} {}".format(r[0], r[1]))


# test()
main()
