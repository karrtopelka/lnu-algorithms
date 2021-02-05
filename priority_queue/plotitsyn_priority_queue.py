# priority queue by Karrtopelka


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, ind, item):
        if self.is_empty():
            self.items.append((ind, item))
        else:
            self.items.append((ind, str(item)))
            self.items.sort(reverse=True)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def print_items(self):
        o = ""
        for i in range(0, len(self.items)):
            o += self.items.pop(0)
        return o


# runner
arr = Queue()
arr.push(3, "Ariana")
arr.push(2, "Rob")
arr.push(4, "Luke")
arr.push(1, "Stacy")
# print(arr.pop())
# arr.print_items()
