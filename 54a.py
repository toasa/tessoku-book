
def solve_a54(queries):
    scores = {}
    for q in queries:
        if q[0] == "1":
            scores[q[1]] = int(q[2])
        else:
            print(scores[q[1]])


def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        q = list(input().split())
        queries.append(q)

    solve_a54(queries)


main()
