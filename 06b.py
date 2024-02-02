N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L, R = [], []
for i in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

hits = [0] * (N+1)
misses = [0] * (N+1)
for i, a in enumerate(A):
    if a == 0:
        hits[i+1] = hits[i]
        misses[i+1] = misses[i] + 1
    else:
        hits[i+1] = hits[i] + 1
        misses[i+1] = misses[i]

for l, r in zip(L, R):
    h = hits[r] - hits[l-1]
    m = misses[r] - misses[l-1]

    if h > m:
        print("win")
    elif h < m:
        print("lose")
    else:
        print("draw")
