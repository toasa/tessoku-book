from enum import Enum


class Type(Enum):
    START = 1
    TERMINAL = 2
    MIDDLE = 3
    MOUNTAIN = 4
    VALLEY = 5


def solve_b38(up_down):
    n_grass = len(up_down) + 1

    if n_grass == 1:
        return 1

    # 隣接する草の高低をグラフ N1->N2 と表す（N1, N2 は草。N2はN1より高いことを表す）。
    # この時、草を5種類に分けることができる：
    #
    #   1.   N->:
    #   2. ->N  :
    #   3. ->N->:
    #   4. ->N<-:
    #   5. <-N->:
    grass_types = [0 for _ in range(n_grass)]

    # 両端の草の種類を決める。
    if up_down[0] == 'A':
        grass_types[0] = Type.START
    else:
        grass_types[0] = Type.TERMINAL
    if up_down[n_grass-2] == 'A':
        grass_types[n_grass-1] = Type.TERMINAL
    else:
        grass_types[n_grass-1] = Type.START

    # 両端以外の草の種類を決める。
    for i in range(1, n_grass-1):
        l = up_down[i-1]
        r = up_down[i]

        if l == 'A' and r == 'B':
            grass_types[i] = Type.MOUNTAIN
        elif l == 'B' and r == 'A':
            grass_types[i] = Type.VALLEY
        else:
            grass_types[i] = Type.MIDDLE

    lengths = [None for _ in range(n_grass)]

    # まず左から右へ草の長さを決める
    for i in range(n_grass):
        if grass_types[i] == Type.START:
            lengths[i] = 1
        elif grass_types[i] == Type.VALLEY:
            lengths[i] = 1
        elif grass_types[i] == Type.MIDDLE:
            l = up_down[i-1]
            r = up_down[i]
            if l == 'A' and r == 'A':
                lengths[i] = lengths[i-1]+1
        elif grass_types[i] == Type.TERMINAL and i == n_grass-1:
            lengths[i] = lengths[i-1]+1

    # 右から左に草の長さを決める
    for i in range(n_grass-1, -1, -1):
        if grass_types[i] == Type.MOUNTAIN:
            lengths[i] = max(lengths[i-1], lengths[i+1])+1
        elif grass_types[i] == Type.MIDDLE and lengths[i] == None:
            lengths[i] = lengths[i+1]+1
        elif grass_types[i] == Type.TERMINAL and lengths[i] == None:
            lengths[i] = lengths[i+1]+1

    return sum(lengths)


def test():
    # solve_b38("AABB")
    # solve_b38("BBAA")
    assert (solve_b38("AABBBA") == 15)
    # solve_b38("BAABBBABBBB")
    # solve_b38("AAA")
    # solve_b38("BBBBB")


def main():
    _ = input()
    up_down = input()
    print(solve_b38(up_down))


# test()
main()
