from random import randint, shuffle

WIN_CONDITIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

MARK_X, MARK_O = 'X', 'O'

CORNERS = [0, 2, 6, 8]
CENTER = 4

board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]
mark = MARK_O


def show_board():
    brd = []
    for i in range(3):
        row = []
        for k in range(3):
            row.append(f' {board[i * 3 + k]} ')
        brd.append(' | '.join(row))
    print(('\n' + '-' * len(brd[0]) + '\n').join(brd))


def user_input() -> int:
    print()
    while True:
        user_inp = input('Выберите клетку для хода: ')
        if user_inp.isdigit() and 1 <= int(user_inp) <= 9 and int(user_inp) in board:
            print()
            return int(user_inp) - 1


def switch_mark():
    global mark
    mark = MARK_O if mark == MARK_X else MARK_X
    return mark


def check_win():
    for combo in WIN_CONDITIONS:
        x, y, z = combo
        row = {board[x], board[y], board[z]}
        if len(row) == 1:
            return board[x]
    return False


def win_turn(current_mark):
    for combo in WIN_CONDITIONS:
        x, y, z = combo
        if board[x] == board[y] == current_mark and isinstance(board[z], int):
            return z
        if board[x] == board[z] == current_mark and isinstance(board[y], int):
            return y
        if board[y] == board[z] == current_mark and isinstance(board[x], int):
            return x


def bot() -> int:
    while True:
        for select_mark in (MARK_O, MARK_X):
            turn = win_turn(select_mark)
            if not turn is None:
                return turn

        if isinstance(board[CENTER], int):
            return CENTER
        shuffle(CORNERS)
        for idx in CORNERS:
            if isinstance(board[idx], int):
                return idx
        bot_turn = randint(0, 8)
        if isinstance(board[bot_turn], int):
            return bot_turn


def start_game():
    user_turn = True
    while True:
        winner = check_win()
        if winner or not any(map(lambda x: isinstance(x, int), board)):
            break
        show_board()
        move = user_input() if user_turn else bot()
        board[move] = switch_mark()
        if not user_turn:
            print(f'\nБот поставил в клетку {move + 1}\n')
        user_turn = False if user_turn else True
    print(f'Победил {winner}!' if winner else 'Ничья!')
    show_board()
    print('\nИгра окончена')


if __name__ == '__main__':
    start_game()
