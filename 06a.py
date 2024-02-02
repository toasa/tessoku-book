N, Q = map(int, input().split())
A = list(map(int, input().split()))
L, R = [], []
for i in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

cumSumA = [0] * (N+1)
for i in range(1, N+1):
    cumSumA[i] = A[i-1] + cumSumA[i-1]

for i in range(Q):
    l = L[i]
    r = R[i]
    print(cumSumA[r]-cumSumA[l-1])
