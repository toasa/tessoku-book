S = input()
T = input()

# dp[i][j] := マス (i, j) に到達するまでに通る、赤い辺の本数の最大値
dp = [[0] * (len(S)+1) for _ in range(len(T)+1)]


for i in range(1, len(T)+1):
    for j in range(1, len(S)+1):
        if S[j-1] == T[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(T)][len(S)])
