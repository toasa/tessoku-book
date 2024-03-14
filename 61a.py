def solve_a61(n_vertices, edges):
    adj_memo = [set() for _ in range(n_vertices+10)]
    for a, b in edges:
        adj_memo[a].add(b)
        adj_memo[b].add(a)

    for v in range(1, n_vertices+1):
        print("{}: {{".format(v), end="")

        l = sorted(list(adj_memo[v]))
        for i, n in enumerate(l):
            if i+1 == len(l):
                print(n, end="")
            else:
                print("{}, ".format(n), end="")
        print("}")


def main():
    #     test("""5 4
    # 1 2
    # 2 3
    # 3 4
    # 3 5""", """1: {2}
    # 2: {1, 3}
    # 3: {2, 4, 5}
    # 4: {3}
    # 5: {3}""")
    #
    #     test("""15 30
    # 6 9
    # 9 10
    # 2 9
    # 9 12
    # 2 14
    # 1 4
    # 4 6
    # 1 3
    # 4 14
    # 1 6
    # 9 11
    # 2 6
    # 3 9
    # 5 9
    # 4 9
    # 11 15
    # 1 13
    # 4 13
    # 8 9
    # 9 13
    # 5 15
    # 3 5
    # 8 10
    # 2 4
    # 9 14
    # 1 9
    # 2 8
    # 6 13
    # 7 9
    # 9 15""", """1: {3, 4, 6, 9, 13}
    # 2: {4, 6, 8, 9, 14}
    # 3: {1, 5, 9}
    # 4: {1, 2, 6, 9, 13, 14}
    # 5: {3, 9, 15}
    # 6: {1, 2, 4, 9, 13}
    # 7: {9}
    # 8: {2, 9, 10}
    # 9: {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15}
    # 10: {8, 9}
    # 11: {9, 15}
    # 12: {9}
    # 13: {1, 4, 6, 9}
    # 14: {2, 4, 9}
    # 15: {5, 9, 11}""")

    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        v1, v2 = map(int, input().split())
        edges.append([v1, v2])

    solve_a61(N, edges)


main()
