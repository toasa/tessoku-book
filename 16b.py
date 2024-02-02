N = int(input())
H = list(map(int, input().split()))
H = [0] + H

# dp[i] := 足場 i にたどり着くまでの最小コスト
dp = [0] * (N+1)
dp[2] = abs(H[2] - H[1])

for i in range(3, N+1):
    dp[i] = min(dp[i-1] + abs(H[i]-H[i-1]), dp[i-2] + abs(H[i]-H[i-2]))

print(dp[N])
