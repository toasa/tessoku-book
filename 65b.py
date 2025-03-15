import sys

sys.setrecursionlimit(10**5)


def dfs(node, ranks, adjs, visited):
    if ranks[node] != -1:
        return ranks[node]

    visited[node] = True

    cur_rank = -1
    subordinates = adjs[node]

    for s in subordinates:
        if visited[s]:
            continue

        subordinate_rank = dfs(s, ranks, adjs, visited)
        if cur_rank < subordinate_rank:
            cur_rank = subordinate_rank

    ranks[node] = cur_rank + 1
    return ranks[node]


def solve_b65(president, relates):
    N = len(relates) + 1

    adjs = [[] for _ in range(N+1)]
    for r1, r2 in relates:
        adjs[r1].append(r2)
        adjs[r2].append(r1)

    ranks = [-1] * (N+1)
    visited = [False] * (N+1)
    dfs(president, ranks, adjs, visited)

    return ranks[1:]


def test():
    assert (
        solve_b65(1,
                  [
                      (1, 2),
                      (1, 3),
                      (3, 4),
                      (2, 5),
                      (4, 6),
                      (4, 7),
                  ])
        ==
        [3, 1, 2, 1, 0, 0, 0]
    )

    assert (
        solve_b65(1,
                  [
                      (1, 2),
                      (2, 3),
                      (1, 4),
                      (1, 5),
                      (1, 6),
                      (6, 7),
                      (2, 8),
                      (6, 9),
                      (9, 10),
                      (10, 11),
                      (6, 12),
                      (12, 13),
                      (13, 14),
                      (12, 15),
                  ])
        ==
        [4, 1, 0, 0, 0, 3, 0, 0, 2, 1, 0, 2, 1, 0, 0]
    )


def main():
    N, president = map(int, input().split())
    relates = []
    for _ in range(N-1):
        r1, r2 = map(int, input().split())
        relates.append((r1, r2))

    res = solve_b65(president, relates)
    print(" ".join(map(str, res)))


# test()
main()
