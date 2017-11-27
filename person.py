from __future__ import print_function
from random import randint
import os


class person:
    def left(self, board_matrix, score, val1, val2):
        if (self.position_y > 0):
            if (board_matrix[self.position_x][self.position_y - 1] == val1):
                os.system('clear')
                print("GAME OVER")

                print("your score is :", score)
                exit(0)

            if (board_matrix[self.position_x][self.position_y - 1] == 0):
                board_matrix[self.position_x][self.position_y] = 0
                board_matrix[self.position_x][self.position_y - 1] = val2
                self.position_y = self.position_y - 1
                return 1
        else:
            return 0

    def right(self, board_matrix, score, val1, val2):
        if (self.position_y < 18):
            if (board_matrix[self.position_x][self.position_y + 1] == val1):
                os.system('clear')
                print("GAME OVER")

                print("your score is :", score)
                exit(0)

            if (board_matrix[self.position_x][self.position_y + 1] == 0):
                board_matrix[self.position_x][self.position_y] = 0
                board_matrix[self.position_x][self.position_y + 1] = val2
                self.position_y = self.position_y + 1
                return 1
        else:
            return 0

    def up(self, board_matrix, score, val1, val2):
        if (self.position_x > 0):
            if (board_matrix[self.position_x - 1][self.position_y] == val1):
                os.system('clear')
                print("GAME OVER")

                print("your score is :", score)
                exit(0)

            if (board_matrix[self.position_x - 1][self.position_y] == 0):
                board_matrix[self.position_x][self.position_y] = 0
                board_matrix[self.position_x - 1][self.position_y] = val2
                self.position_x = self.position_x - 1
                return 1
        else:
            return 0

    def down(self, board_matrix, score, val1, val2):
        if (self.position_x < 16):
            if (board_matrix[self.position_x + 1][self.position_y] == val1):
                os.system('clear')
                print("GAME OVER")

                print("your score is :", score)
                exit(0)

            if (board_matrix[self.position_x + 1][self.position_y] == 0):
                board_matrix[self.position_x][self.position_y] = 0
                board_matrix[self.position_x + 1][self.position_y] = val2
                self.position_x = self.position_x + 1
                return 1
        else:
            return 0


class bomberman(person):
    position_x = 0

    position_y = 0
    alive = 1

    def __init__(self, board_matrix, score):
        board_matrix[self.position_x][self.position_y] = 4


class enemy(person):
    position_x = 0
    position_y = 0

    def __init__(self, board_matrix, score):

        i = 0
        while (i == 0):
            v = randint(0, 16)
            w = 0
            if (v % 2 == 0):
                w = randint(0, 18)
                if ((v + w) > 1 and board_matrix[v][w] == 0):
                    board_matrix[v][w] = 3
                    i = 1
            else:
                w = randint(1, 10)
                w = w * 2 - 2
                if ((v + w) > 1):
                    if (board_matrix[v][w] == 0):
                        board_matrix[v][w] = 3
                        i = 1
        self.position_x = v
        self.position_y = w
        self.move = [self.left, self.right, self.up, self.down]

    def move_enemy(self, board_matrix, score):
        p = randint(0, 3)

        for i in range(4):
            if (self.move[((p + i) % 4)](board_matrix, score, 4, 3) == 1):
                break
