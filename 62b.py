def solve_b62(n_node, edges):
    adjs = [[] for _ in range(n_node + 10)]
    for e1, e2 in edges:
        adjs[e1].append(e2)
        adjs[e2].append(e1)

    src_map = [0 for _ in range(n_node + 10)]
    visited = [False for _ in range(n_node + 10)]
    stack = [1]

    while len(stack) > 0:
        node = stack.pop()
        visited[node] = True

        if node == n_node:
            break

        for adj in adjs[node]:
            if not visited[adj]:
                src_map[adj] = node
                stack.append(adj)

    node = n_node
    route = [node]
    while node != 1:
        node = src_map[node]
        route.append(node)

    route.reverse()

    return " ".join(map(str, route))


def test():
    assert (
        solve_b62(5, [
            (1, 2),
            (2, 3),
            (3, 4),
            (3, 5),
        ])
        ==
        "1 2 3 5"
    )

    assert (
        solve_b62(15, [
            (6, 9),
            (9, 10),
            (2, 9),
            (9, 12),
            (2, 14),
            (1, 4),
            (4, 6),
            (1, 3),
            (4, 14),
            (1, 6),
            (9, 11),
            (2, 6),
            (3, 9),
            (5, 9),
            (4, 9),
            (11, 15),
            (1, 13),
            (4, 13),
            (8, 9),
            (9, 13),
            (5, 15),
            (3, 5),
            (8, 10),
            (2, 4),
            (9, 14),
            (1, 9),
            (2, 8),
            (6, 13),
            (7, 9),
            (9, 15),
        ])
        ==
        "1 9 15"
    )


def main():
    n_node, n_edge = map(int, input().split())
    edges = []
    for _ in range(n_edge):
        n1, n2 = map(int, input().split())
        edges.append((n1, n2))

    print(solve_b62(n_node, edges))


# test()
main()
