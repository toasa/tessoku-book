T = int(input())
N = int(input())
L, R = [], []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

delta = [0] * (T + 2)

for l, r in zip(L, R):
    delta[l] += 1
    delta[r] -= 1

count = 0
for t in range(T):
    count += delta[t]
    print(count)
