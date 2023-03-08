import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()

Q = int(input())
for _ in range(Q):
    x = int(input())
    print(bisect.bisect_left(A, x))
