# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

import random as rd

# шахматная доска без ферзей
def form_chessboard(rows, columns):
    return [['*'] * columns for _ in range(rows)]

# рисование шахматной доски
def drawing_chessboard(matrix):
    for row in range(len(matrix)):                    
        for column in range(len(matrix[row])):
            print(matrix[row][column], end = ' ')
        print()

# шахматная доска с ферзями
def form_chessboard_with_queens(matrix, coords_list):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            for item in range(len(coords_list)):
                if row + 1 == coords_list[item][0] and column + 1 == coords_list[item][1]:
                    matrix[row][column] = 'Q'
    return matrix

# проверка на то, бьют ли ферзи друг друга
def beat_queens(coords_list):
    for i in range(len(coords_list)):
        next_coords_list = coords_list[(i+1):]
        for j in range(len(next_coords_list)):
            if coords_list[i][0] == next_coords_list[j][0] or \
                coords_list[i][1] == next_coords_list[j][1] or \
                abs(coords_list[i][0] - next_coords_list[j][0]) == abs(coords_list[i][1] - next_coords_list[j][1]):
                return False
    return True

def form_coords(rows, columns):
    return [[rd.randint(1, 8) for j in range(columns)] for i in range(rows)]













