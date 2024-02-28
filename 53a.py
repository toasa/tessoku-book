import heapq


def solve_a53(queries):
    hq = []
    for q in queries:
        if q[0] == "1":
            heapq.heappush(hq, int(q[2:]))
        elif q[0] == "2":
            print(hq[0])
        else:
            heapq.heappop(hq)


def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        q = input()
        queries.append(q)

    solve_a53(queries)


main()
