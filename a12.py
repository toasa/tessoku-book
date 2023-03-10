N, K = map(int, input().split())
A = list(map(int, input().split()))


def n_sheets(d):
    sum = 0
    for a in A:
        sum += d // a
    return sum


def main():
    l = 1
    r = 1_000_000_000
    while l < r:
        mid = (l + r) // 2
        n = n_sheets(mid)
        if n >= K:
            r = mid
        else:
            l = mid + 1

    print(l)


main()
