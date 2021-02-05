# sparse matrix by Karrtopelka ^)^)^)^^^^)))))))

import random as rnd


def checker(st, en):
    if max(st, en) == st:
        print("Start can't be smaller than end, you know...")
        return False
    return True


def create_null_matrix():
    tmp = []
    for m in range(0, rows):
        tmp.append([0]*rows)
    return tmp


def fill(row, count, el=0, chance=1):
    while el < count:
        if chance != 0:
            matrix[rnd.randint(0, row - 1)][rnd.randint(0,
                                                        row - 1)] = rnd.randint(s, e)
            el += 1
            count -= 1
        else:
            break
        chance = rnd.randint(0, 25)


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
s = int(input("Tell me, from which number I need to start: "))
e = int(input("And where I need to end: "))
if checker(s, e):
    print("Now I am going to randomly fill sparse matrix with some numbers ({} - {})".format(s, e))
    fill(rows, pow(rows, 2))
    printer()
