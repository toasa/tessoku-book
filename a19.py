N, W = map(int, input().split())

# dp[i][j] := 品物 0, 1, ..., i のなかからいくつかを選ぶときに、重さが j 以下となる価値の最大値
dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = map(int, input().split()) 
    for j in range(1, W+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])
