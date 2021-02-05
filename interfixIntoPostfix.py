# postfix Макса ^)^)^)^^)^)^)^)^)^)
# ───==≡≡ΣΣ((( つºل͜º)つ

from stack import Stack


def postfix(expr):
    priority = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
    my_stack = Stack()
    inter_expr = expr.split(" ")
    out = []

    for token in inter_expr:
        if token.isnumeric() or token.isalpha():
            out.append(token)
        elif token == "(":
            my_stack.push(token)
        elif token == ")":
            top_token = my_stack.pop()
            while top_token != "(":
                out.append(top_token)
                top_token = my_stack.pop()
        else:
            while not my_stack.empty() and priority[my_stack.peek()] >= priority[token]:
                out.append(my_stack.pop())
            my_stack.push(token)

    while not my_stack.empty():
        out.append(my_stack.pop())
    return " ".join(out)


# example_wth_letters = "( A + B ) * ( C + M )"
# example_wth_numbers = "22 - ( 17 ^ 2 - 17 * ( 15 + 1 ) )"
# print(postfix(example_wth_letters) + '\n' + postfix(example_wth_numbers))
