N = int(input())
points = [[0] * (2000) for _ in range(2000)]
for _ in range(N):
    x, y = map(int, input().split())
    points[x][y] += 1

cumSum = [[0] * (2000) for _ in range(2000)]

for x in range(1, 2000):
    for y in range(1, 2000):
        cumSum[x][y] = cumSum[x][y-1] + \
            cumSum[x-1][y] - cumSum[x-1][y-1]
        # cumSum[x][y] += 1 if points[x-1][y-1] else 0
        cumSum[x][y] += points[x-1][y-1]

Q = int(input())

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    sum = cumSum[c+1][d+1] - cumSum[a][d+1] - cumSum[c+1][b] + cumSum[a][b]
    print(sum)
