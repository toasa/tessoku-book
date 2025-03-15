import heapq


def solve_b64(N, adjs, weights):
    src_map = [0] * (N+10)
    visited = [False] * (N+10)
    move_cost = [2**60] * (N+10)
    move_cost[1] = 0

    q = []
    heapq.heappush(q, (0, 1))  # ヒープキューの中身は、(移動コスト, 頂点) のタプル

    while len(q) > 0:
        cost_cur, node = heapq.heappop(q)
        if visited[node]:
            continue

        visited[node] = True

        if node == N:
            break

        for adj in adjs[node]:
            if visited[adj]:
                continue

            if move_cost[adj] <= cost_cur + weights[(node, adj)]:
                continue

            src_map[adj] = node
            move_cost[adj] = cost_cur + weights[(node, adj)]
            heapq.heappush(q, (move_cost[adj], adj))

    shortest_route = [N]
    node = N
    while node != 1:
        node = src_map[node]
        shortest_route.append(node)

    shortest_route.reverse()

    print(" ".join(map(str, shortest_route)))


def main():
    N, M = map(int, input().split())
    adjs = [[] for _ in range(N+10)]
    weights = {}

    for _ in range(M):
        v1, v2, w = map(int, input().split())

        adjs[v1].append(v2)
        adjs[v2].append(v1)

        weights[(v1, v2)] = w
        weights[(v2, v1)] = w

    solve_b64(N, adjs, weights)


main()
