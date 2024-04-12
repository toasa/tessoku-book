# めぐる式二分探索の実装
# 参考資料： https://qiita.com/drken/items/97e37dd6143e33a64c8c

#  needle <= haystack[i] (条件A) となるようなインデックス i のうち、最小の i を返す
#
# l と r　は以下の条件を満たしつつ、更新していく
# * l は常に (条件A) を満たさない
# * r は常に (条件A) を満たす
def bisearch_meguru(haystack, needle):
    l = -1
    r = len(haystack)
    while r-l > 1:
        mid = (l+r)//2
        if needle <= haystack[mid]:
            r = mid
        else:
            l = mid
    return r


def solve_b10(arr, queries):
    arr.sort()
    res = []
    for q in queries:
        def is_ok(i): return q <= arr[i]
        res.append(bisearch_meguru(arr, q))
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


test()
