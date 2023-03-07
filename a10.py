N = int(input())
A = list(map(int, input().split()))
D = int(input())
L, R = [], []
for _ in range(D):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

maxL = [0] * (N + 2)
maxR = [0] * (N + 2)
for i in range(1, N+1):
    maxL[i] = max(maxL[i-1], A[i-1])
    maxR[N-i+1] = max(maxR[N-i+2], A[N-i])

for l, r in zip(L, R):
    print(max(maxL[l-1], maxR[r+1]))
