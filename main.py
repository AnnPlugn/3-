import warnings
import random
import universal
import db

warnings.filterwarnings("ignore")


def print_odd_numbers():
    A = input('Введите через пробел список чисел: ').split()
    lst = [int(i) for i in A]
    spisok = []
    for num in lst:
        if num % 2 != 0:
            spisok.append(num)
        elif num == 71278:
            break
    print(spisok)
    db.save_result('Список1: ', spisok)
    return


def gen_spisok():
    A = input('Введите через пробел список чисел: ').split()
    lst = [int(i) for i in A if int(i) != 500]
    print(lst)
    db.save_result('Список2: ', lst)
    return


def unique_list():
    unique_lst = random.sample(range(100), 50)
    print(unique_list)
    db.save_result('Список3: ', unique_lst)
    return


def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу и БД, результат сохранить в MySQL.
2. Нечетные числа списка, результат сохранить в MySQL.
3. Числа списка кроме 500, результат сохранить в MySQL.
4. Список случайных чисел, результат сохранить в MySQL.
5. Сохранить все данные из MySQL в Excel.
6. Завершить"""
    while run:
        run = universal.uni(commands,
                            db.check_db, print_odd_numbers, gen_spisok, unique_list,
                            db.save_db_to_xlsx)
    return


if __name__ == '__main__':
    main()
