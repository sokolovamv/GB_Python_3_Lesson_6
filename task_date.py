# Создайте модуль и напишите в нем функцию, которая получает на вход дату в формате DD.MM.YYYY 
# Функция возваращает истину, если дата может существовать или ложь, если такая дата невозможна 
# Для простоты договоримся, что год может быть в диапазоне [1,9999] 
# Весь  период (1 января 1 года - 31 декабря 9999 года) действует григорианский календарь 
# Проверку года на високосность  вынести в отдельную защищенную функцию
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import time
from sys import argv


def _leap_check(in_date: str) -> bool:
    return False if not int(in_date[7:]) % 100 and int(in_date[7:]) % 400 else (True if not int(in_date[7:]) % 4 else False)

def date_check(in_date: str) -> bool:
    try:
        time.strptime(in_date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


date_entered = argv[1]

print(date_check(date_entered))

if __name__ == '__main__':
    if _leap_check(date_entered):
        print('Високосный год')
    else:
        print('Невисокосный год')