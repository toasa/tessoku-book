from random import randint


def solve_b13(items, yosan):
    cumsum = 0
    res = 0

    r = 0
    for l in range(len(items)):
        # l を固定し、右開区間 items[l:r) が条件を満たすように r をインクリメントする。
        while r < len(items) and 0 < cumsum+items[r] <= yosan:
            cumsum += items[r]
            r += 1
            # ここで res += 1 とカウントしていくのは何故うまくいかないか？
            # => あー、そりゃそうか
            # => このループを抜けてから res += r-l するというのは、以下の区間を数え上げてるのか：
            #    items[l:i], items[l:i+1], ..., items[l:r]

        res += r-l

        if r == l:
            # r が更新されなかった場合。
            # 次の区間の探索に向け l==r となるように r を進める。
            r += 1
        else:
            # r が更新された場合。
            # l をインクリメントする前に、累積和を減らす。
            cumsum -= items[l]

    return res


def solve_b13_slow(items, yosan):
    res = 0
    for h in range(1, len(items)+1):
        for t in range(h):
            if sum(items[t:h]) <= yosan:
                res += 1
    return res


def test():
    assert (
        solve_b13([10], 50)
        ==
        1
    )

    assert (
        solve_b13([10], 5)
        ==
        0
    )

    assert (
        solve_b13([11, 12, 16, 22, 27, 28, 31], 50)
        ==
        13
    )

    assert (
        solve_b13([33, 11, 50, 1, 53], 15)
        ==
        2
    )

    assert (
        solve_b13([70, 59, 77, 66, 97, 44, 99, 53, 13, 76], 66)
        ==
        6
    )

    # # Fuzzing test
    # yosan = randint(0, 100)
    # items = []
    # for _ in range(5):
    #     items.append(randint(0, 100))

    # actual = solve_b13(items, yosan)
    # expected = solve_b13_slow(items, yosan)
    # assert actual == expected, "items: {}, yosan: {}, expected: {}, actual: {}".format(
    #     items,
    #     yosan,
    #     expected,
    #     actual)


def main():
    _, yosan = map(int, input().split())
    items = list(map(int, input().split()))

    print(solve_b13(items, yosan))


# test()
main()
