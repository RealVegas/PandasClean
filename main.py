# Задание: Исследование оценок учеников
# Представьте, что у вас есть таблица из 10 учеников с оценками
# по 5 разным предметам.
# Вам нужно проанализировать эти данные:
# 1. Создайте DataFrame с данными;
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться,
#    что данные загружены правильно;
# 3. Вычислите среднюю оценку по каждому предмету;
# 4. Вычислите медианную оценку по каждому предмету;
# 5. Вычислите Q1,Q3 и IQR для оценок по математике;
# 6. Вычислите стандартное отклонение.

from pandas import Series, DataFrame
from random import randint, shuffle


def task():

    pupils: list[str] = ['Саша', 'Таня', 'Петя', 'Ваня', 'Лена', 'Оля', 'Лиза', 'Марина', 'Алеша', 'Даша']
    subjects: list[str] = ['Математика', 'Физика', 'Информатика', 'Химия', 'Английский', 'Математика', 'Физика', 'Информатика', 'Химия', 'Английский']
    shuffle(subjects)

    marks: list[int] = [randint(3, 5) for _ in range(10)]

    dframe: DataFrame = DataFrame({'Имя': Series(pupils), 'Предмет': Series(subjects), 'Оценка': Series(marks)})

    print('Первые 5 строк из DataFrame:')
    print(dframe.head())
    print('\nСредняя оценка по предметам:')
    print(dframe.groupby('Предмет')['Оценка'].mean())
    print('\nМедианная оценка по предметам:')
    print(dframe.groupby('Предмет')['Оценка'].median())

    q1: float = dframe[dframe['Предмет'] == 'Математика']['Оценка'].quantile(0.25)
    q3: float = dframe[dframe['Предмет'] == 'Математика']['Оценка'].quantile(0.75)
    iqr: float = q3 - q1

    print(f'\nQ1 по математике = {q1}')
    print(f'Q3 по математике = {q3}')
    print(f'IQR по математике = {iqr}')

    # Список предметов
    by_subject: list[str] = list(dframe['Предмет'].unique())

    print('\nСтандартное отклонение по каждому предмету:')
    for subject in by_subject:
        print(f'{subject} = {dframe[dframe["Предмет"] == subject]["Оценка"].std()}')


if __name__ == "__main__":
    task()