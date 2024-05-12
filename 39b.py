import heapq


def solve_b39(n_day, works):
    # 開始日が早い順にソート
    works.sort(key=lambda w: w[0])

    res = 0
    work_heap = []
    w_i = 0

    for d in range(1, n_day+1):
        while w_i < len(works) and works[w_i][0] <= d:
            w = works[w_i]

            # 給料に関する max-heap を作る：
            heapq.heappush(work_heap, (-1*w[1], w[0]))
            w_i += 1

        if len(work_heap) > 0:
            w = heapq.heappop(work_heap)
            res += -1 * w[0]

    return res


def test():
    assert (
        solve_b39(
            4,
            [
                (1, 1),
                (2, 4),
                (2, 3),
                (3, 4),
                (4, 2),
            ]
        )
        ==
        12
    )


def main():
    N, D = map(int, input().split())
    works = []
    for _ in range(N):
        start_day, wage = map(int, input().split())
        works.append((start_day, wage))

    print(solve_b39(D, works))


# test()
main()
