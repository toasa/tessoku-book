class Movie:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.len = end - start


def solve_a39(N, L, R):
    movies = []
    for l, r in zip(L, R):
        movies.append(Movie(l, r))

    # movies.sort(key=lambda m: m.start)
    # movies.sort(key=lambda m: m.len)
    movies.sort(key=lambda m: m.end)

    # まずは貪欲法でやってみる。
    res = 0
    cur_end = -1
    for m in movies:
        if m.start >= cur_end:
            res += 1
            cur_end = m.end

    return res


def main():
    # assert (solve_a39(5, [0, 2, 3, 5, 7], [4, 3, 7, 9, 8]) == 3)

    N = int(input())
    L, R = [], []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    print(solve_a39(N, L, R))


main()
