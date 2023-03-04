N = int(input())
deltas = [[0] * (2000) for _ in range(2000)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    deltas[a][b] += 1
    deltas[c+1][d+1] += 1

    deltas[a][d+1] -= 1
    deltas[c+1][b] -= 1


cumSum = [[0] * (2000) for _ in range(2000)]
for h in range(1, 2000):
    for w in range(1, 2000):
        cumSum[h][w] = cumSum[h-1][w] + cumSum[h][w-1] - \
            cumSum[h-1][w-1] + deltas[h-1][w-1]

area = 0
for h in range(1800):
    for w in range(1800):
        if cumSum[h][w] >= 1 and cumSum[h+1][w] >= 1 and cumSum[h][w+1] >= 1 and cumSum[h+1][w+1] >= 1:
            area += 1

print(area)
