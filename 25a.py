H, W = map(int, input().split())

squares = [""]
for _ in range(H):
    s = input()
    s = "." + s
    squares.append(s)

dp = [[0] * (W+1) for _ in range(H+1)]

nstep = 1
for h in range(1, H+1):
    if squares[h][1] == "#":
        nstep = 0
    dp[h][1] = nstep

nstep = 1
for w in range(1, W+1):
    if squares[1][w] == "#":
        nstep = 0
    dp[1][w] = nstep

for h in range(2, H+1):
    for w in range(2, W+1):
        if squares[h][w] == "#":
            continue
        dp[h][w] += dp[h-1][w] + dp[h][w-1]

print(dp[H][W])

# for r in dp:
#     print(r)
