N, X = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = N
while abs(l - r) >= 2:
    mid = (l + r) // 2
    if A[mid] <= X:
        l = mid
    else:
        r = mid

print(l + 1)
