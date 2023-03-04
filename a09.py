H, W, N = map(int, input().split())
deltas = [[0] * (W + 2) for _ in range(H + 2)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    deltas[a][b] += 1
    deltas[c+1][d+1] += 1

    deltas[a][d+1] -= 1
    deltas[c+1][b] -= 1


cumSum = [[0] * (W+1) for _ in range(H+1)]
for h in range(1, H+1):
    for w in range(1, W+1):
        cumSum[h][w] = cumSum[h-1][w] + cumSum[h][w-1] - \
            cumSum[h-1][w-1] + deltas[h][w]

for h in range(1, H+1):
    for w in range(1, W+1):
        if w == W:
            print(cumSum[h][w])
        else:
            print(str(cumSum[h][w]) + " ", end="")
