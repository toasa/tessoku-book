def solve_b09(coords):
    LEN = 1510
    cum_sum_map = [[0 for _ in range(LEN)] for _ in range(LEN)]

    for x1, y1, x2, y2 in coords:
        cum_sum_map[x1][y1] += 1
        cum_sum_map[x2][y2] += 1
        cum_sum_map[x1][y2] -= 1
        cum_sum_map[x2][y1] -= 1

    for h in range(LEN):
        for w in range(1, LEN):
            cum_sum_map[h][w] += cum_sum_map[h][w-1]

    for w in range(LEN):
        for h in range(1, LEN):
            cum_sum_map[h][w] += cum_sum_map[h-1][w]

    res = 0
    for h in range(LEN):
        for w in range(LEN):
            if cum_sum_map[h][w] > 0:
                res += 1

    return res


def test():
    assert (
        solve_b09(
            [
                [1, 1, 3, 3],
            ]
        )
        ==
        4
    )

    assert (
        solve_b09(
            [
                [1, 1, 3, 3],
                [2, 2, 4, 4],
            ]
        )
        ==
        7
    )

    assert (
        solve_b09(
            [
                [1, 1, 5, 5],
                [3, 3, 7, 6],
            ]
        )
        ==
        24
    )


def main():
    N = int(input())
    coords = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        coords.append([x1, y1, x2, y2])

    print(solve_b09(coords))


# test()
main()
