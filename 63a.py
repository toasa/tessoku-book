from collections import deque


def solve_a63(n_vertices, edges):
    adj_vertices = [[] for _ in range(n_vertices+10)]

    for edge in edges:
        v1, v2 = edge
        adj_vertices[v1].append(v2)
        adj_vertices[v2].append(v1)

    TMP_MAX = 10**5 + 1
    min_edges = [TMP_MAX for _ in range(n_vertices+10)]

    reached = [False for _ in range(n_vertices+10)]

    queue = deque([(1, 0)])
    min_edges[1] = 0
    reached[1] = True

    while len(queue) > 0:
        v, n_edge_cur = queue.popleft()

        for adj_v in adj_vertices[v]:
            if not reached[adj_v]:
                reached[adj_v] = True
                min_edges[adj_v] = min(n_edge_cur+1, min_edges[adj_v])

                queue.append((adj_v, n_edge_cur+1))

    res = []
    for v in range(1, n_vertices+1):
        res.append(min_edges[v] if min_edges[v] != TMP_MAX else -1)

    return res


def main():
    # assert (solve_a63(3, [[1, 3], [2, 3]]) == [0, 2, 1])

    # assert (
    #     solve_a63(
    #         6,
    #         [
    #             [1, 4],
    #             [2, 3],
    #             [3, 4],
    #             [5, 6],
    #             [1, 2],
    #             [2, 4],
    #         ]
    #     )
    #     ==
    #     [0, 1, 2, 1, -1, -1]
    # )

    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        v1, v2 = map(int, input().split())
        edges.append([v1, v2])

    res = solve_a63(N, edges)
    for r in res:
        print(r)


main()
