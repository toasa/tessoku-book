def solve_a43(L, positions, directions):
    res = -1
    for position, direction in zip(positions, directions):
        if direction == "E":
            duration = L - position
        else:
            duration = position
        res = max(res, duration)

    return res


def main():
    # assert (solve_a43(100, [20, 50, 70], ["E", "E", "W"]) == 80)

    N, L = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = input().split()
        A.append(int(a))
        B.append(b)
    print(solve_a43(L, A, B))


main()
