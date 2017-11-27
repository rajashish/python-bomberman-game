import os


class bomb:
    def __init__(self, board_matrix, x, y, score, enemy_array):
        self.x = x
        self.y = y
        board_matrix[self.x][self.y] = 6
        self.bomb_array = [[self.x, self.y]]
        self.bomb_array_val = [board_matrix[self.x][self.y]]
        if (self.y > 0):
            if (board_matrix[self.x][self.y - 1] == 4):
                self.bomb_array.append([self.x, self.y - 1])
                self.bomb_array_val.append(board_matrix[self.x][self.y - 1])

            if (board_matrix[self.x][self.y - 1] == 2):
                self.bomb_array.append([self.x, self.y - 1])
                self.bomb_array_val.append(board_matrix[self.x][self.y - 1])

            if (board_matrix[self.x][self.y - 1] == 3):
                self.bomb_array.append([self.x, self.y - 1])
                self.bomb_array_val.append(board_matrix[self.x][self.y - 1])
            if (board_matrix[self.x][self.y - 1] == 0):
                self.bomb_array.append([self.x, self.y - 1])
                self.bomb_array_val.append(board_matrix[self.x][self.y - 1])

        if (self.x > 0):
            if (board_matrix[self.x - 1][self.y] == 4):
                self.bomb_array.append([self.x - 1, self.y])
                self.bomb_array_val.append(board_matrix[self.x - 1][self.y])

            if (board_matrix[self.x - 1][self.y] == 2):
                self.bomb_array.append([self.x - 1, self.y])
                self.bomb_array_val.append(board_matrix[self.x - 1][self.y])

            if (board_matrix[self.x - 1][self.y] == 3):
                self.bomb_array.append([self.x - 1, self.y])
                self.bomb_array_val.append(board_matrix[self.x - 1][self.y])
            if (board_matrix[self.x - 1][self.y] == 0):
                self.bomb_array.append([self.x - 1, self.y])
                self.bomb_array_val.append(board_matrix[self.x - 1][self.y])

        if (self.y < 18):
            if (board_matrix[self.x][self.y + 1] == 4):
                self.bomb_array.append([self.x, self.y + 1])
                self.bomb_array_val.append(board_matrix[self.x][self.y + 1])

            if (board_matrix[self.x][self.y + 1] == 2):
                self.bomb_array.append([self.x, self.y + 1])
                self.bomb_array_val.append(board_matrix[self.x][self.y + 1])

            if (board_matrix[self.x][self.y + 1] == 3):
                self.bomb_array.append([self.x, self.y + 1])
                self.bomb_array_val.append(board_matrix[self.x][self.y + 1])
            if (board_matrix[self.x][self.y + 1] == 0):
                self.bomb_array.append([self.x, self.y + 1])
                self.bomb_array_val.append(board_matrix[self.x][self.y + 1])

        if (self.x < 16):
            if (board_matrix[self.x + 1][self.y] == 4):
                self.bomb_array.append([self.x + 1, self.y])
                self.bomb_array_val.append(board_matrix[self.x + 1][self.y])

            if (board_matrix[self.x + 1][self.y] == 2):
                self.bomb_array.append([self.x + 1, self.y])
                self.bomb_array_val.append(board_matrix[self.x + 1][self.y])

            if (board_matrix[self.x + 1][self.y] == 3):
                self.bomb_array.append([self.x + 1, self.y])
                self.bomb_array_val.append(board_matrix[self.x + 1][self.y])
            if (board_matrix[self.x + 1][self.y] == 0):
                self.bomb_array.append([self.x + 1, self.y])
                self.bomb_array_val.append(board_matrix[self.x + 1][self.y])

    def explosion(self, board_matrix, enemy_array, score):
        if (self.y > 0):
            if (board_matrix[self.x][self.y - 1] == 4):
                os.system('clear')
                print("GAME OVER")
                print
                "your score is :", score
                exit(0)

            if (board_matrix[self.x][self.y - 1] == 2):
                score = score + 20
            if (board_matrix[self.x][self.y - 1] == 3):
                for i in enemy_array:
                    if i.position_x == self.x and i.position_y == self.y - 1:
                        enemy_array.remove(i)
                        score = score + 50
        if (self.x > 0):
            if (board_matrix[self.x - 1][self.y] == 4):
                os.system('clear')
                print("GAME OVER")
                print("your score is :", score)
                exit(0)
            if (board_matrix[self.x - 1][self.y] == 2):
                score = score + 20
            if (board_matrix[self.x - 1][self.y] == 3):

                for i in enemy_array:
                    if (i.position_x == self.x - 1 and i.position_y == self.y):
                        enemy_array.remove(i)
                        score = score + 50

        if (self.y < 18):
            if (board_matrix[self.x][self.y + 1] == 4):
                os.system('clear')
                print("GAME OVER")
                print
                "your score is :", score
                exit(0)
            if (board_matrix[self.x][self.y + 1] == 2):
                score = score + 20
            if (board_matrix[self.x][self.y + 1] == 3):

                for i in enemy_array:
                    if (i.position_x == self.x and i.position_y == self.y + 1):
                        enemy_array.remove(i)
                        score = score + 50

        if (self.x < 16):
            if (board_matrix[self.x + 1][self.y] == 4):
                os.system('clear')
                print("GAME OVER")
                print
                "your score is :", score
                exit(0)
            if (board_matrix[self.x + 1][self.y] == 2):
                score = score + 20
            if (board_matrix[self.x + 1][self.y] == 3):

                for i in enemy_array:
                    if (i.position_x == self.x + 1 and i.position_y == self.y):
                        enemy_array.remove(i)
                        score = score + 50

        if (board_matrix[self.x][self.y] == 4):
            os.system('clear')
            print("GAME OVER")
            print
            "your score is :", score
            exit(0)
        return score
