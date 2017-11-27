from __future__ import print_function
import time
from board import *
from person import *
from time import time
from inp import *
from bomb import *
import os

score = 0
live = 1


def level(enemy_count, enemy_time, bomberman_time, levels):
    board_matrix = [[0 for j in range(19)] for i in range(17)]
    global score
    b = Board(board_matrix)

    b.printboard(board_matrix, score, levels)
    p = bomberman(board_matrix, score)
    b.printboard(board_matrix, score, levels)
    enemy_array = []
    for i in range(enemy_count):
        enemy_array.append(enemy(board_matrix, score))

    explosion_time = 3.6
    bomberman_ptime = time()
    enemy_ptime = time()
    bomb_plant_time = time() - 3.6
    bomb_plant = 0
    bmbx = 0
    bmby = 0
    while (1):
        if (enemy_array.__len__() == 0):
            break

        current_time = time()
        if ((current_time - bomberman_ptime) < bomberman_time):
            c = char.getch()

        if ((current_time - bomberman_ptime) > bomberman_time):

            inp = char.getch()

            if (inp == 'w'):
                p.up(board_matrix, score, 3, 4)
            elif (inp == 's'):
                p.down(board_matrix, score, 3, 4)
            elif (inp == 'd'):
                p.right(board_matrix, score, 3, 4)
            elif (inp == 'a'):
                p.left(board_matrix, score, 3, 4)
            elif (inp == 'q'):
                os.system('clear')
                print("your score is :", score)
                print("END")
                exit(0)
            elif (inp == 'b' or inp == ' '):
                if (current_time - bomb_plant_time > explosion_time):
                    bomb_plant = 1
                    bomb_plant_time = current_time
                    bmbx = p.position_x
                    bmby = p.position_y
                    bmb = bomb(board_matrix, bmbx, bmby, score, enemy_array)

            bomberman_ptime = current_time

            b.printboard(board_matrix, score, levels)

        if (bomb_plant == 1):
            cmp = current_time - bomb_plant_time

            if (cmp < 0.6):
                board_matrix[bmbx][bmby] = 6
                b.printboard(board_matrix, score, levels)
            if (cmp >= 0.6 and cmp < 1.2):
                board_matrix[bmbx][bmby] = 7
                b.printboard(board_matrix, score, levels)
            if (cmp >= 1.2 and cmp < 1.8):
                board_matrix[bmbx][bmby] = 8
                b.printboard(board_matrix, score, levels)
            elif (cmp >= 1.8 and cmp < 2.4):
                # bmb.get_bomb_area(board_matrix,enemy_array)
                board_matrix[p.position_x][p.position_y] = 4
                score = bmb.explosion(board_matrix, enemy_array, score)
                for i in bmb.bomb_array:
                    board_matrix[i[0]][i[1]] = 9
                b.printboard(board_matrix, score, levels)
            elif (cmp >= 2.4):

                for i in bmb.bomb_array:
                    board_matrix[i[0]][i[1]] = 0
                b.printboard(board_matrix, score, levels)
                bomb_plant = 0

        if ((current_time - enemy_ptime) > enemy_time):

            for i in enemy_array:
                i.move_enemy(board_matrix, score)

            b.printboard(board_matrix, score, levels)
            enemy_ptime = current_time


level(4, 0.4, 0.3, 1)
level(6, 0.35, 0.25, 2)
level(8, 0.3, 0.2, 3)
level(10, 0.25, 0.15, 4)
level(12, 0.2, 0.1, 5)

os.system('clear')
print("CONGRATULATIONS")
print("GAME COMPLETED")

print("your score is :", score)
exit(0)
