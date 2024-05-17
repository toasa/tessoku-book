from collections import deque


def solve_b52(balls, X):
    queue = deque([])

    # まず、キューに整数 X を追加し、ボール X を青で塗る。
    # その後、キューが空になるまで以下の操作を繰り返す。
    #   - キューの先頭要素 ( pos) を削除する
    #   - ボール pos−1 が白のとき、これを青で塗り、キューに pos−1 を追加する
    #   - ボール pos+1 が白のとき、これを青で塗り、キューに pos+1 を追加する

    queue.append(X-1)
    balls[X-1] = '@'  # -1 はインデックス合わせ

    while len(queue) > 0:
        pos = queue.popleft()
        if 0 <= pos-1 and balls[pos-1] == ".":
            balls[pos-1] = '@'
            queue.append(pos-1)
        if pos+1 < len(balls) and balls[pos+1] == ".":
            balls[pos+1] = '@'
            queue.append(pos+1)

    return "".join(balls)


def test():
    assert (
        solve_b52(
            list("#...#"),
            3
        )
        ==
        "#@@@#"
    )


def main():
    _, X = map(int, input().split())
    balls = list(input())

    print(solve_b52(balls, X))


# test()
main()
