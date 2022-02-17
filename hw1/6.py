# Без применения готовых библиотек, написать алгоритм, который позволяет
# вводить  матрицу  (указывается  размер  и  значения  элементов),  а  затем  по
# желанию  пользователя  выполнять  возведение  в  квадрат  (если  возможно),
# транспонировать   (если   возможно),   для   квадратной   матрицы   находить
# определитель.
def input_matrix():
    a, b = map(int, input().split())
    matrix = [[0] * b] * a
    for i in range(a):
        matrix[i] = list(map(int, input().split()))
    return matrix


def output_matrix(matrix):
    output = ""
    for i in matrix:
        output += ' '.join(list(map(str, i))) + "\n"
    return output


def square_matrix(matrix):
    a = len(matrix)
    b = len(matrix[0])
    if a != b:
        return [[None]]
    out = [[0 for i in range(a)] for i in range(a)]
    for i in range(a):
        for j in range(a):
            for key in range(a):
                out[i][j] += matrix[i][key] * matrix[key][j]
    return out


def transport_matrix(matrix):
    a = len(matrix)
    b = len(matrix[0])
    out = [[0 for i in range(a)] for i in range(b)]
    for i in range(b):
        for j in range(a):
            out[i][j] = matrix[j][i]
    return out


def local_matrix(matrix, element_a, element_b):
    matrix_new = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix_new[i][j] = matrix[i][j]
    del matrix_new[element_a]
    for line in matrix_new:
        del line[element_b]
    return matrix_new


def opredelitel_matrix(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        a = len(matrix)
        answer = 0
        znak = 1
        key = 0
        for i in range(a):
            for j in range(a):
                answer += matrix[key][j] * znak * opredelitel_matrix(local_matrix(matrix, i, j))
                znak *= -1

    return answer


print("введите размерность матрицы фомата a b, и ее элементы построчно через пробел ")
matrix = input_matrix()
print("вывод матрицы")
print(output_matrix(matrix))
print("квадрат матрицы")
print(output_matrix(square_matrix(matrix)))
print("транспонированная матрица")
print(output_matrix(transport_matrix(matrix)))
print("определитель матрицы")
print(opredelitel_matrix(matrix))
