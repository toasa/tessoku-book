H, W = map(int, input().split())
X = [[0] * W for _ in range(H)]

for h in range(H):
    xs = list(map(int, input().split()))
    X[h] = xs

Q = int(input())

A, B, C, D = [], [], [], []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

cumSumX = [[0] * (W+1) for _ in range(H+1)]
for h in range(1, H+1):
    for w in range(1, W+1):
        cumSumX[h][w] = cumSumX[h][w-1] + \
            cumSumX[h-1][w] - cumSumX[h-1][w-1] + X[h-1][w-1]

for q in range(Q):
    a, b, c, d = A[q], B[q], C[q], D[q]
    sum = cumSumX[c][d] - cumSumX[a-1][d] - cumSumX[c][b-1] + cumSumX[a-1][b-1]
    print(sum)
