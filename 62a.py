def solve_a62(n_vertices, edges):
    adjs = [set() for _ in range(n_vertices+10)]
    for a, b in edges:
        adjs[a].add(b)
        adjs[b].add(a)
    for i, adj in enumerate(adjs):
        if len(adj) == 0:
            adjs[i] = list()
        else:
            adjs[i] = sorted(list(adj))

    # 頂点 1 からスタート
    stack = [1]
    reached = [False for _ in range(n_vertices+10)]
    reached[1] = True
    n_reached = 0
    while len(stack) > 0:
        v = stack.pop()

        n_reached += 1
        # print("now: {}, n_reached: {}".format(v, n_reached))
        if n_reached == n_vertices:
            return "The graph is connected."

        for adj_v in adjs[v]:
            if not reached[adj_v]:
                # print("   append({})".format(adj_v))
                reached[adj_v] = True
                stack.append(adj_v)

    return "The graph is not connected."


def main():
    # assert (
    #     solve_a62(3, [[1, 3], [2, 3]])
    #     == "The graph is connected.")

    # assert (
    #     solve_a62(6, [[1, 4], [2, 3], [3, 4], [5, 6], [1, 2], [2, 4]])
    #     == "The graph is not connected.")

    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append([a, b])

    print(solve_a62(N, edges))


main()
