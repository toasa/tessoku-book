def solve_a15(arr):
    index_map = {}
    for i, a in enumerate(arr):
        if a not in index_map:
            index_map[a] = []

        index_map[a].append(i)

    arr.sort()

    res = [0 for _ in range(len(arr))]

    a_count = {}
    for a in arr:
        a_count[a] = 0

    cur = 1
    for a in arr:
        i = index_map[a][a_count[a]]
        res[i] = cur

        a_count[a] += 1

        # a が arr の中に一個だけある場合、もしくは複数個でその最後の要素の場合
        if len(index_map[a]) == a_count[a]:
            cur += 1

    return res


def test():
    assert (
        solve_a15([10])
        ==
        [1]
    )

    assert (
        solve_a15([10, 10])
        ==
        [1, 1]
    )

    assert (
        solve_a15([1, 10, 10])
        ==
        [1, 2, 2]
    )

    assert (
        solve_a15([10, 10, 15])
        ==
        [1, 1, 2]
    )

    assert (
        solve_a15([46, 80, 11, 77, 46])
        ==
        [2, 4, 1, 3, 2]
    )


def main():
    _ = input()
    A = list(map(int, input().split()))

    res = solve_a15(A)
    for i, r in enumerate(res):
        if i + 1 != len(res):
            print("{} ".format(r), end="")
        else:
            print(r)


# test()
main()
