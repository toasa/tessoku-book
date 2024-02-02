D = int(input())
N = int(input())
L, R = [], []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

cumSum = [0] * (D+2)
for l, r in zip(L, R):
    cumSum[l] += 1
    cumSum[r+1] -= 1

count = 0
for d in range(1, D+1):
    count += cumSum[d]
    print(count)
