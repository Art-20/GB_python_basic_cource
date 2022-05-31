# Задание 1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
# виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix


    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                   for i in range(len(self.matrix))]
        return Matrix(result)


    def __str__(self):
        out = "| "
        for i in self.matrix:
            out = f'{out}'
            for j in i:
                out = f'{out}{j} '
            out = f'{out}| \n| '
        return out[:-2]


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
    print(fail_matrix)
    print(fail_matrix+first_matrix)