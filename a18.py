N, S = map(int, input().split())
A = list(map(int, input().split()))
A = [0] + A

# dp[i][j] := カード 0, 1, 2, ..., i の中から何枚か選び、合計を j にすることは可能か？
dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(0, S+1):
        if j < A[i]:
            if dp[i-1][j]:
                dp[i][j] = True
        else:
            if dp[i-1][j] or dp[i-1][j - A[i]]:
                dp[i][j] = True

print("Yes" if dp[N][S] else "No")
