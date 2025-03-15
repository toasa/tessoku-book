import heapq


def solve_a64(n_vertices, edges):
    dists = {}
    adjs = [[] for _ in range(n_vertices+10)]
    for v1, v2, d in edges:
        adjs[v1].append(v2)
        adjs[v2].append(v1)

        dists[(v1, v2)] = d
        dists[(v2, v1)] = d

    INF = 2 ** 32
    move_costs = [INF for _ in range(n_vertices+10)]
    move_costs[1] = 0

    q = []
    heapq.heappush(q, (0, 1))  # ヒープキューの中身は、(移動コスト、頂点)のタプル

    visited = [False] * (n_vertices+10)

    while len(q) > 0:
        cur_cost, node = heapq.heappop(q)

        if visited[node]:
            continue

        visited[node] = True

        for adj in adjs[node]:
            if move_costs[adj] <= cur_cost + dists[(node, adj)]:
                continue

            move_costs[adj] = cur_cost + dists[(node, adj)]
            heapq.heappush(q, (move_costs[adj], adj))

    res = []
    for v in range(1, n_vertices+1):
        res.append(move_costs[v] if move_costs[v] != INF else -1)
    return res


def test():
    assert (
        solve_a64(
            2,
            [
                [1, 2, 10],
            ]
        )
        ==
        [0, 10]
    )

    assert (
        solve_a64(
            3,
            [
                [2, 3, 10],
            ]
        )
        ==
        [0, -1, -1]
    )

    assert (
        solve_a64(
            4,
            [
                [1, 2, 10],
                [2, 3, 20],
            ]
        )
        ==
        [0, 10, 30, -1]
    )

    assert (
        solve_a64(
            6,
            [
                [1, 2, 15],
                [1, 4, 20],
                [2, 3, 65],
                [2, 5, 4],
                [3, 6, 50],
                [4, 5, 30],
                [5, 6, 8],
            ]
        )
        ==
        [0, 15, 77, 20, 19, 27]
    )

    assert (
        solve_a64(
            15,
            [
                [10, 11, 23],
                [11, 13, 24],
                [5, 8, 22],
                [10, 15, 18],
                [12, 14, 15],
                [2, 10, 11],
                [4, 7, 15],
                [5, 7, 15],
                [7, 9, 8],
                [8, 12, 1],
                [5, 14, 1],
                [10, 14, 17],
                [10, 12, 11],
                [8, 10, 6],
                [7, 14, 28],
                [6, 9, 1],
                [1, 10, 19],
                [4, 5, 4],
                [9, 10, 21],
                [7, 10, 21],
                [4, 10, 29],
                [5, 10, 8],
                [4, 14, 8],
                [11, 12, 24],
                [10, 13, 13],
                [3, 10, 1],
                [5, 12, 24],
                [2, 15, 23],
                [6, 10, 18],
                [6, 15, 25],
            ]
        )
        ==
        [0, 30, 20, 31, 27, 37, 40, 25, 38, 19, 42, 26, 32, 28, 37]
    )


def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        v1, v2, d = map(int, input().split())
        edges.append([v1, v2, d])

    res = solve_a64(N, edges)
    for r in res:
        print(r)


# test()
main()
