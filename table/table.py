# tables Максааа
# ___________________________________
# |^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ||____
# | The Karrtopelka Truck!        |||""'|""\__,_
# | _____________________________ l||___|__|__|)
# |(@)@)"""""""''''''''''''''**|(@)(@)*****|(@)
import random

table_main = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}


def to_num(string):
    return int(string) if float(string) == int(float(string)) else float(string)


def checker(num):
    try:
        int(num)
        return True
    except ValueError:
        try:
            float(num)
            return True
        except ValueError:
            print("not a number!")
            return False


def int_r(numb):
    numb = int(numb + (0.5 if numb > 0 else -0.5))
    return numb


def table_maker(number):
    if checker(number):
        operating_num = to_num(number)
        temp = str(int_r(operating_num))
        last = int(temp[-1])
        if last in table_main:
            table_main[last].append(operating_num)


# runner
print("Input range number: ")
range_start = int(input())

print("Input range number: ")
range_end = int(input())

print("Input range to: ")
range_end_i = int(input())


for i in range(0, range_end_i):
    ind = str(random.randrange(range_start, range_end))
    table_maker(ind)


table_maker("17.3")
table_maker("17.6")


print("our table:")
for i, v in sorted(table_main.items()):
    print("{}: {}".format(i, v))
