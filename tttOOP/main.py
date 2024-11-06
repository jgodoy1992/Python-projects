from TTTOOP import Board


def main():

    board = Board(6)
    board.build_board()

    while True:

        board.user_move()

        if board.is_victory('O'):
            print('Usuario gana')
            break

        board.draw_move()

        if board.is_victory('X'):
            print('Maquina gana')

        if len(board.list_of_free_cells()) == 0:
            print('Empate')
            break


if __name__ == '__main__':
    main()
