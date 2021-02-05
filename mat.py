# розріджена matrix by Max

import time as tm
import random as rnd


def create_null_matrix():
    matrix_temp = []
    for m in range(0, rows):
        matrix_temp.append([])
    for i in range(0, len(matrix_temp)):
        for k in range(0, len(matrix_temp)):
            matrix_temp[i].append(0)
    return matrix_temp


def fill(row, count, el=0, ch=1):
    while el < count:
        if ch != 0:
            matrix[rnd.randint(0, row - 1)][rnd.randint(0, row - 1)] = rnd.randint(0, 100)
            el += 1
            count -= 1
        else:
            break
        ch = rnd.randint(0, 25)


def printer():
    for w in range(0, rows):
        print(matrix[w])


# Runner
print("Hello!")
rows = int(input("Size of matrix: "))
print("ok")
print("creating null matrix")
matrix = create_null_matrix()
print("done")
s = int(input("Tell me from which number I need to start: "))
e = int(input("And also end number: "))
print("Now I am going to randomly fill matrix with some numbers ({} - {})".format(s, e))
fill(rows, pow(rows, 2))
printer()
