# Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import eight_queens as eq


rows_on_chessboard = 8
columns_on_chessboard = 8
number_of_queens = 8
coordinate_system = 2
count = 0


while count < 4:
    list_of_queens_coordinates = eq.form_coords(number_of_queens, coordinate_system)
    #list_of_queens_coordinates = [[1, 7], [2, 4], [3, 2], [4, 8], [5, 6], [6, 1], [7, 3], [8, 5]]
    chessboard = eq.form_chessboard(rows_on_chessboard, columns_on_chessboard)
    chessboard = eq.form_chessboard_with_queens(chessboard, list_of_queens_coordinates)
    if eq.beat_queens(list_of_queens_coordinates) ==  True:
        count += 1
        print(list_of_queens_coordinates)
        eq.drawing_chessboard(chessboard)
        print(eq.beat_queens(list_of_queens_coordinates))
        