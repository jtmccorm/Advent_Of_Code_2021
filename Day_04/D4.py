# AOC_2021
# author: @jtmccorm
import numpy as np


class BingoBoard:
    def __init__(self, numbers):
        self.numbers = np.array(numbers)
        self.activation = np.zeros_like(self.numbers)

    def activate(self, number):
        idx = np.where(self.numbers == number)
        try:
            row_idx, col_idx = idx[0][0], idx[1][0]
            self.activation[row_idx][col_idx] = 1
            # print("found")
        except:
            pass

    def check_win(self):
        row_sums = np.sum(self.activation, axis=1)
        col_sums = np.sum(self.activation, axis=0)
        row_check = np.sum(col_sums == 5) > 0
        col_check = np.sum(row_sums == 5) > 0
        # print(row_check, col_check)
        return row_check or col_check

    def unmarked_sum(self):
        unmarked_idx = np.where(self.activation==0)
        unmarked_numbers = self.numbers[unmarked_idx]
        return np.sum(unmarked_numbers)


if __name__ == '__main__':
    # extract and format the input
    input_txt = [line for line in open("D4_input.txt")]
    bingo_numbers = [int(txt) for txt in input_txt.pop(0).split(',')]
    potential_boards = []
    board_array = []
    for i in range(1, len(input_txt)):
        if i % 6 == 0:
            potential_boards.append(BingoBoard(board_array))
            board_array = []
        else:
            board_array.append([int(txt) for txt in input_txt[i].rstrip().split()])

    no_winner = True
    loser_found = False
    for number in bingo_numbers:
        if loser_found: break
        boards_to_remove = []
        for board in potential_boards:
            board.activate(number)
            if board.check_win():
                if len(potential_boards) == 1:
                    losing_board = board
                    losing_number = number
                    print("Loser Found!")
                    loser_found = True
                    break
                else:
                    if no_winner:
                        winning_board = board
                        winning_number = number
                        no_winner = False
                    boards_to_remove.append(board)
        for board in boards_to_remove: potential_boards.remove(board)

    # Part 1 - find the winning board
    print(f"Winning Board:\n", winning_board.numbers,"\n" ,winning_board.activation)
    print(f"Sum={winning_board.unmarked_sum()}, Number={winning_number}, Product={winning_board.unmarked_sum() * winning_number}")

    # Part 2 - find the losing board
    print(f"Losing Board:\n", losing_board.numbers,"\n" ,losing_board.activation)
    print(f"Sum={losing_board.unmarked_sum()}, Number={losing_number}, Product={losing_board.unmarked_sum() * losing_number}")
