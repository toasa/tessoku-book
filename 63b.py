from collections import deque


def solve_b63(start, goal, maze):
    start = (start[0]-1, start[1]-1)
    goal = (goal[0]-1, goal[1]-1)

    n_row = len(maze)
    n_col = len(maze[0])
    min_step = [[2 << 60 for _ in range(n_col + 10)]
                for _ in range(n_row + 10)]
    min_step[start[0]][start[1]] = 0

    q = deque([start])
    while len(q) > 0:
        now = q.popleft()

        if now == goal:
            break

        nexts = [
            (now[0]-1, now[1]),
            (now[0], now[1]-1),
            (now[0]+1, now[1]),
            (now[0], now[1]+1),
        ]

        for next in nexts:
            if (0 <= next[0] < n_row) and (0 <= next[1] < n_col):
                if maze[next[0]][next[1]] == '#':
                    continue

                if min_step[now[0]][now[1]] + 1 < min_step[next[0]][next[1]]:
                    min_step[next[0]][next[1]] = min_step[now[0]][now[1]] + 1
                    q.append(next)

    # for s in min_step:
    #     print(s)

    return min_step[goal[0]][goal[1]]


def main():
    n_row, _ = map(int, input().split())
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    maze = []
    for _ in range(n_row):
        r = input()
        maze.append(r)

    print(solve_b63(start, goal, maze))


def test():
    assert (
        solve_b63(
            (2, 2),
            (4, 5),
            [
                "########",
                "#......#",
                "#.######",
                "#..#...#",
                "#..##..#",
                "##.....#",
                "########",
            ])
        ==
        11
    )

    assert (
        solve_b63(
            (2, 2),
            (2, 4),
            [
                "########",
                "#.#....#",
                "#.###..#",
                "#......#",
                "########",
            ])
        ==
        10
    )

    assert (
        solve_b63(
            (2, 2),
            (11, 11),
            [
                "############",
                "#..........#",
                "#..........#",
                "#..........#",
                "#..........#",
                "#..........#",
                "#..........#",
                "#..........#",
                "#..........#",
                "#..........#",
                "#..........#",
                "############",
            ])
        ==
        18
    )


# test()
main()
