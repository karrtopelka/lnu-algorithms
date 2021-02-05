# Стек Макса :)
# ..*.*... \O/..*..*
# *.....*...|....*...
# *......../.\....*..*


# клас
class Stack:
    # вхідні значення
    def __init__(self):
        self.items = []

    # перевірка чи пустий стек чи ні
    def empty(self):
        return self.items == []

    # присвоюєм стеку значення
    def push(self, item):
        self.items.append(item)

    # вилучаєм зі стеку значення
    def pop(self):
        return self.items.pop()

    # піковий елемент, береться останній максимальний індекс масиву
    def peek(self):
        return self.items[len(self.items) - 1]

    # розмір стеку
    def size(self):
        return len(self.items)

    # виведення всіх елементів стеку
    def print_all_items(self):
        return ", ".join(self.items)


# my_stack = Stack()
#
# # засовуєм в стек елементи
# my_stack.push('burger')
# my_stack.push('cheese')
# my_stack.push('beer')
# my_stack.push('milk')
#
# print("внесли 4 елементи:")
# my_stack.print_all_items()
# print("\nподивимось розмір стеку: {0}\nперевіримо чи пустий: {1}".format(my_stack.size(), my_stack.empty()))
# print("\nперевіримо піковий елемент: {0}".format(my_stack.peek()))
# print("\nвилучимо елемент: {0}, і подивимось який елемент став піковим: {1}".format(my_stack.pop(), my_stack.peek()))
# print("наш стек:")
# my_stack.print_all_items()
# print("\nзалишимо один елемент в стеці: {0}, {1} - видалено".format(my_stack.pop(), my_stack.pop()))
# print("\nподивимось розмір стеку: {0}\nвилучимо останній елемент: {1}".format(my_stack.size(), my_stack.pop()))
# print("\nперевіримо чи пустий: {0}".format(my_stack.empty()))
