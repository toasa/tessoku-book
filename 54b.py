def solve_b54(As):
    count = {}

    for a in As:
        if a not in count:
            count[a] = 1
        else:
            count[a] += 1

    res = 0
    for n in count.values():
        if n >= 2:
            res += n*(n-1)//2

    return res


def test():
    assert (
        solve_b54([30, 10, 30, 20, 10, 30])
        ==
        4
    )


def main():
    N = int(input())

    res = []
    for _ in range(N):
        n = int(input())
        res.append(n)

    print(solve_b54(res))


# test()
main()
