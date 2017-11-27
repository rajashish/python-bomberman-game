from __future__ import print_function
from random import randint


class Board:
    x = 17
    y = 19

    def __init__(self, board_matrix):
        for i in range(self.x):
            for j in range(self.y):
                if (i % 2 == 1 and j % 2 == 1):
                    board_matrix[i][j] = 1
        for i in range(40):
            v = randint(0, 16)
            w = 0
            if (v % 2 == 0):
                w = randint(0, 18)
                if ((v + w) > 1):
                    board_matrix[v][w] = 2
            else:
                w = randint(1, 10)
                if ((v + w * 2 - 2) > 1):
                    board_matrix[v][w * 2 - 2] = 2

    def printboard(self, board_matrix, score, level):
        print("LEVEL :", level)
        print("your score is ", score)
        print("press q to end the game")
        for i in range(2):
            for j in range(4 * self.y + 8):
                print('\x1b[0;37;47m' + "X" + '\x1b[0m', end="")
            print("\n", end="")
        for i in range(2 * self.x):
            print('\x1b[0;37;47m' + "XXXX" + '\x1b[0m', end="")
            for j in range(4 * self.y):
                p = i // 2
                q = j // 4
                if (board_matrix[p][q] == 1):
                    print('\x1b[0;37;47m' + "X" + '\x1b[0m', end="")
                elif (board_matrix[p][q] == 2):
                    print('\x1b[0;37;42m' + "%" '\x1b[0m', end="")
                elif (board_matrix[p][q] == 4):
                    print('\x1b[1;34;44m' + "B" + '\x1b[0m', end="")
                elif (board_matrix[p][q] == 3):
                    print('\x1b[1;32;41m' + "E" + '\x1b[0m', end="")
                elif (board_matrix[p][q] == 6):
                    print('\x1b[1;30;43m' + "3" + '\x1b[0m', end="")
                elif (board_matrix[p][q] == 7):
                    print('\x1b[1;34;43m' + "2" + '\x1b[0m', end="")
                elif (board_matrix[p][q] == 8):
                    print('\x1b[1;37;43m' + "1" + '\x1b[0m', end="")

                elif (board_matrix[p][q] == 9):
                    print('\x1b[1;31;43m' + "0" + '\x1b[0m', end="")

                else:
                    print(" ", end="")
            print('\x1b[0;37;47m' + "XXXX" + '\x1b[0m')

        for i in range(2):
            for j in range(4 * self.y + 8):
                print('\x1b[0;37;47m' + "X" + '\x1b[0m', end="")
            print("\n", end="")
        for i in range(3):
            print("\n", end="")
