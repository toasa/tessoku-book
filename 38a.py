def solve_a38(D, N, L, R, H):
    max_working_times = [24] * (D+10)

    for i in range(N):
        l, r, h = L[i], R[i], H[i]
        for j in range(l, r+1):
            max_working_times[j] = min(max_working_times[j], h)

    return sum(max_working_times[1:(D+1)])


def main():
    # assert (solve_a38(5, 3, [1, 2, 3], [2, 3, 5], [22, 16, 23]) == 100)

    D, N = map(int, input().split())
    L, R, H = [], [], []
    for _ in range(N):
        l, r, h = map(int, input().split())
        L.append(l)
        R.append(r)
        H.append(h)

    print(solve_a38(D, N, L, R, H))


main()
