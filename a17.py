N = int(input())
A = list(map(int, input().split()))
A = [0, 0] + A
B = list(map(int, input().split()))
B = [0, 0, 0] + B

# dp[i] := 部屋1 から部屋 i までの最短移動時間
dp = [0] * (N + 1)
dp[2] = A[2]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])

cur_room = N
passed_rooms = []

while cur_room != 1:
    passed_rooms.append(cur_room)

    if cur_room == 2:
        break

    if dp[cur_room] == dp[cur_room-1] + A[cur_room]:
        cur_room -= 1
    else:
        cur_room -= 2

passed_rooms.append(1)

print(len(passed_rooms))

for i in range(len(passed_rooms)):
    if i == len(passed_rooms) - 1:
        print(passed_rooms[0])
    else:
        print(passed_rooms[len(passed_rooms)-i-1], end="")
        print(" ", end="")
