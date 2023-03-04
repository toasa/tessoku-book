N = int(input())
A = list(map(int, input().split()))


def main():
    for i in range(N-2):
        for j in range(i + 1, N-1):
            for k in range(j + 1, N):
                s = A[i] + A[j] + A[k]
                if s == 1000:
                    print("Yes")
                    return
    print("No")


main()
