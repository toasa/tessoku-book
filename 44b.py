def solve_b44(grid, queries):
    res = []

    for q in queries:
        query_type = q[0]

        if query_type == 1:
            # list の index が 0 始まりのため、調整
            row1 = q[1]-1
            row2 = q[2]-1
            grid[row1], grid[row2] = grid[row2], grid[row1]
        else:
            x = q[1]-1
            y = q[2]-1
            res.append(grid[x][y])

    return res


def test():
    assert (
        solve_b44(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [
                [2, 2, 1],
                [1, 1, 2],
                [2, 2, 1],
                [2, 1, 3],
                [1, 2, 3],
                [2, 2, 3],
                [2, 3, 2],
            ]
        )
        ==
        [4, 1, 6, 9, 2]
    )


def main():
    N = int(input())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    n_query = int(input())
    queries = []
    for _ in range(n_query):
        q = list(map(int, input().split()))
        queries.append(q)

    res = solve_b44(grid, queries)
    for r in res:
        print(r)


# test()
main()
