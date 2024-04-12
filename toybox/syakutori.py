def syakutori(items, yosan):
    cumsum = 0
    res = 0

    r = 0
    for l in range(len(items)):
        # l を固定し、右開区間 items[l:r) が条件を満たすように r をインクリメントする。
        while r < len(items) and 0 < cumsum+items[r] <= yosan:
            cumsum += items[r]
            r += 1

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


def test():
    assert (
        syakutori([10], 50)
        ==
        1
    )

    assert (
        syakutori([10], 5)
        ==
        0
    )

    assert (
        syakutori([11, 12, 16, 22, 27, 28, 31], 50)
        ==
        13
    )

    assert (
        syakutori([33, 11, 50, 1, 53], 15)
        ==
        2
    )

    assert (
        syakutori([70, 59, 77, 66, 97, 44, 99, 53, 13, 76], 66)
        ==
        6
    )


test()
