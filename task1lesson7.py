import random
import itertools


class Matrix:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def __str__(self):
        for el in self.numbers_list:
            print(el)
        return ""

    def __add__(self, other):
        result_matrix = []
        for i in range(len(self.numbers_list)):
            result_matrix.append([j + k for j, k in zip(self.numbers_list[i], other.numbers_list[i])])
        return result_matrix


def create_matrix(row_count, col_count, data_list):
    matrix = []
    for i in range(row_count):
        row_list = []
        for j in range(col_count):
            row_list.append(data_list[row_count*i+j])
        matrix.append(row_list)

    return matrix


def creation():
    matrix_list = [random.randint(0, 9) for el in range(36)]
    result_matrix = create_matrix(6, 6, matrix_list)
    return result_matrix


matrix_obj = Matrix(creation())
print(matrix_obj)
matrix_2 = Matrix(creation())
print(matrix_2)

print(matrix_obj+matrix_2)
