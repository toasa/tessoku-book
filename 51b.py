def solve_b51(S):
    stack = []

    res = []

    for i, c in enumerate(S):
        if c == '(':
            stack.append(i)
        else:
            l = stack.pop()
            res.append((l+1, i+1))

    return res


def test():
    assert (
        solve_b51("(())()")
        ==
        [(2, 3), (1, 4), (5, 6)]
    )


def main():
    S = input()

    res = solve_b51(S)
    for r in res:
        print("{} {}".format(r[0], r[1]))


# test()
main()
