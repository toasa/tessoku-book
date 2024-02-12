def solve_a33(N, A):
    return "First"


def kosatsu_a33():
    SIZE = 20

    is_first_move_win = [
        [[True for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]

    for i in range(SIZE):
        is_first_move_win[i][i][0] = False
        is_first_move_win[i][0][i] = False
        is_first_move_win[0][i][i] = False

    for i in range(1, SIZE):
        for j in range(1, i+1):
            for k in range(1, j+1):
                # print("[{}, {}, {}] enter".format(i, j, k))

                found_win_move = False

                for n_take in range(1, k+1):
                    # print("  [{}, {}, {}] check => {}".format(
                    #     i, j, k-n_take, is_first_move_win[i][j][k-n_take]))
                    if not is_first_move_win[i][j][k-n_take]:
                        found_win_move = True
                        break
                if found_win_move:
                    break

                for n_take in range(1, j+1):
                    #  print("  [{}, {}, {}] check => {}".format(
                    #      i, j-n_take, k, is_first_move_win[i][j-n_take][k]))
                    if not is_first_move_win[i][j-n_take][k]:
                        found_win_move = True
                        break
                if found_win_move:
                    break

                for n_take in range(1, i+1):
                    #  print("  [{}, {}, {}] check => {}".format(
                    #      i-n_take, j, k, is_first_move_win[i-n_take][j][k]))
                    if not is_first_move_win[i-n_take][j][k]:
                        found_win_move = True
                        break
                if found_win_move:
                    break

                is_first_move_win[i][j][k] = False
                is_first_move_win[i][k][j] = False
                is_first_move_win[j][i][k] = False
                is_first_move_win[j][k][i] = False
                is_first_move_win[k][i][j] = False
                is_first_move_win[k][j][i] = False
                print("[{}, {}, {}] is MUST LOSE".format(i, j, k))

    # for r in is_first_move_win:
    #     print("=====")
    #     for c in r:
    #         print(c)


def main():
    kosatsu_a33()

    # assert (solve_a33(2, [7, 7]) == "Second")
    # assert (solve_a33(2, [5, 8]) == "First")


main()
