# postfix evaluation Макса :)):):):):)):)
# (　・ω・)⊃-[二> >二]-⊂(´∀｀ )

from interfixIntoPostfix import postfix
from stack import Stack


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
        if token.isnumeric():
            my_stack.push(token)
        else:
            op2 = int(my_stack.pop())
            op1 = int(my_stack.pop())
            result = evaluation(op1, op2, token)
            my_stack.push(result)
    return my_stack.pop()


interfix_expression = "22 - ( 17 ^ ( 2 - 17 * ( 15 + 1 ) ) - 17 * ( 15 + 1 ) )"
postfix_expresion = postfix(interfix_expression)
postfix_result = postfix_evaluation(postfix_expresion)
print("Our interfix expression = {}".format(interfix_expression))
print("Our postfix expression = {}".format(postfix_expresion))
print("The result is: {}".format(postfix_result))
