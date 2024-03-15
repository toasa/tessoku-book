from collections import deque


def solve_a64(n_vertices, edges):
    INF = 2 ** 32
    # dists = [[INF for _ in range(n_vertices+10)] for _ in range(n_vertices+10)]
    dists = {}

    adjs = [[] for _ in range(n_vertices+10)]
    for v1, v2, d in edges:
        adjs[v1].append(v2)
        adjs[v2].append(v1)
        dists[(v1, v2)] = d

    # 頂点1からスタート
    queue = deque([(1, 0)])

    min_dist = [INF for _ in range(n_vertices+10)]
    min_dist[1] = 0

    while len(queue) > 0:
        v, cur_dist = queue.popleft()

        for adj in adjs[v]:
            next_dist = dists[(v, adj)] if v < adj else dists[(adj, v)]
            d = cur_dist + next_dist
            if d < min_dist[adj]:
                min_dist[adj] = d
                queue.append((adj, d))

    res = []
    for v in range(1, n_vertices+1):
        res.append(min_dist[v] if min_dist[v] != INF else -1)
    return res


def main():
    # assert (
    #     solve_a64(
    #         2,
    #         [
    #             [1, 2, 10],
    #         ]
    #     )
    #     ==
    #     [0, 10]
    # )

    # assert (
    #     solve_a64(
    #         3,
    #         [
    #             [2, 3, 10],
    #         ]
    #     )
    #     ==
    #     [0, -1, -1]
    # )

    # assert (
    #     solve_a64(
    #         4,
    #         [
    #             [1, 2, 10],
    #             [2, 3, 20],
    #         ]
    #     )
    #     ==
    #     [0, 10, 30, -1]
    # )

    # assert (
    #     solve_a64(
    #         6,
    #         [
    #             [1, 2, 15],
    #             [1, 4, 20],
    #             [2, 3, 65],
    #             [2, 5, 4],
    #             [3, 6, 50],
    #             [4, 5, 30],
    #             [5, 6, 8],
    #         ]
    #     )
    #     ==
    #     [0, 15, 77, 20, 19, 27]
    # )

    # assert (
    #     solve_a64(
    #         15,
    #         [
    #             [10, 11, 23],
    #             [11, 13, 24],
    #             [5, 8, 22],
    #             [10, 15, 18],
    #             [12, 14, 15],
    #             [2, 10, 11],
    #             [4, 7, 15],
    #             [5, 7, 15],
    #             [7, 9, 8],
    #             [8, 12, 1],
    #             [5, 14, 1],
    #             [10, 14, 17],
    #             [10, 12, 11],
    #             [8, 10, 6],
    #             [7, 14, 28],
    #             [6, 9, 1],
    #             [1, 10, 19],
    #             [4, 5, 4],
    #             [9, 10, 21],
    #             [7, 10, 21],
    #             [4, 10, 29],
    #             [5, 10, 8],
    #             [4, 14, 8],
    #             [11, 12, 24],
    #             [10, 13, 13],
    #             [3, 10, 1],
    #             [5, 12, 24],
    #             [2, 15, 23],
    #             [6, 10, 18],
    #             [6, 15, 25],
    #         ]
    #     )
    #     ==
    #     [0, 30, 20, 31, 27, 37, 40, 25, 38, 19, 42, 26, 32, 28, 37]
    # )

    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        v1, v2, d = map(int, input().split())
        edges.append([v1, v2, d])

    res = solve_a64(N, edges)
    for r in res:
        print(r)


main()
