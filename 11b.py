# arr[i] >= x となるようなインデックス i のうち、最小の i を返す
def bisearch_meguru(arr, is_ok):
    l = -1
    r = len(arr)
    while r-l > 1:
        mid = (l+r)//2
        if is_ok(mid):
            r = mid
        else:
            l = mid
    return r


def solve_b10(arr, queries):
    arr.sort()
    res = []
    for q in queries:
        def is_ok(i): return q <= arr[i]
        res.append(bisearch_meguru(arr, is_ok))
    return res


def test():
    assert (
        solve_b10(
            [5],
            [1, 5, 10]
        )
        == [0, 0, 1]
    )

    assert (
        solve_b10(
            [83, 31, 11, 17, 32, 19, 23, 37, 43, 47, 53, 61, 67, 5, 55],
            [10, 20, 30, 40, 50]
        )
        == [1, 4, 5, 8, 10]
    )

    assert (
        solve_b10(
            [2, 3, 3, 3, 2],
            [4, 3, 2]
        )
        == [5, 2, 0]
    )


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        q = int(input())
        queries.append(q)

    res = solve_b10(arr, queries)
    for r in res:
        print(r)


# test()
main()
