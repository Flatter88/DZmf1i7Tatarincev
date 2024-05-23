import numpy as np

def read_matrix_from_file(nazvanie):
    with open(nazvanie, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.strip().split())) for line in lines]
    return np.array(matrix)

def product_of_nonzero_elements(vector):
    product = 1
    for element in vector:
        if element != 0:
            product *= element
    return product

def find_max_product_column(matrix):
    max_product = -1
    max_column_index = -1
    for i in range(matrix.shape[1]):
        column = matrix[:, i]
        product = product_of_nonzero_elements(column)
        if product > max_product:
            max_product = product
            max_column_index = i
    return max_column_index

def extract_column(matrica, column_index):
    return matrica[:, column_index]

filename = 'matrica.txt'
matrix = read_matrix_from_file(filename)
max_column_index = find_max_product_column(matrix)
max_column = extract_column(matrix, max_column_index)
print(max_column)