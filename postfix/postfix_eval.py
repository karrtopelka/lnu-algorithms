from math import sqrt
from postfix import postfix, checker
from stack import Stack


def num(string):
    return int(string) if float(string) == int(float(string)) else float(string)


def evaluation(op1, op2, token):
    if token == "+":
        return op1 + op2
    elif token == "*":
        return op1 * op2
    elif token == "/":
        return op1 / op2
    elif token == "^":
        return pow(op1, op2)
    else:
        return op1 - op2


def postfix_evaluation(post_expr):
    my_stack = Stack()
    post_expr = post_expr.split()

    for token in post_expr:
        if checker(token):
            my_stack.push(token)
        elif token == '#':
            my_stack.push(sqrt(num(my_stack.pop())))
        elif token == "|":
            my_stack.push(abs(num(my_stack.pop())))
        else:
            op2 = num(my_stack.pop())
            op1 = num(my_stack.pop())
            result = evaluation(op1, op2, token)
            my_stack.push(result)
    return "{:.2f}".format(my_stack.pop())


infix_expression = input("Expression\n")
postfix_expresion = postfix(infix_expression)
postfix_result = postfix_evaluation(postfix_expresion)
print("Infix: {}".format(infix_expression))
print("Postfix: {}".format(postfix_expresion))
print("Result: {}".format(postfix_result))

