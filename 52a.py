from collections import deque


def solve_a52(queries):
    queue = deque([])
    for q in queries:
        if q[0] == "1":
            queue.append(q[2:])
        elif q[0] == "2":
            print(queue[0])
        else:
            queue.popleft()


def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        q = input()
        queries.append(q)

    solve_a52(queries)


main()
