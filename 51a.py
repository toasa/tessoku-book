def solve_a51(queries):
    stack = []
    for q in queries:
        if q[0] == "1":
            stack.append(q[2:])
        elif q[0] == "2":
            print(stack[len(stack)-1])
        else:
            stack.pop()


def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        q = input()
        queries.append(q)

    solve_a51(queries)


main()
