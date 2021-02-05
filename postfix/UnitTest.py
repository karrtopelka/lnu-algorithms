from unittest import TestCase

from stack import Stack


# tests for stack
class TestStack(TestCase):
    def setUp(self):
        self.my_stack = Stack()


class TestAllStack(TestStack):
    def test_initial_items(self):
        self.assertEqual(self.my_stack.items, [])

    def test_check_empty(self):
        self.my_stack.push("Hello")
        self.assertEqual(self.my_stack.empty(), False)

    def test_push(self):
        self.my_stack.push("Hello")
        self.assertEqual(self.my_stack.size(), 1)

    def test_pop(self):
        self.my_stack.push("Hello")
        self.my_stack.push("World")
        self.my_stack.pop()
        self.assertEqual(self.my_stack.peek(), "Hello")

    def test_peek(self):
        self.my_stack.push("Hello")
        self.my_stack.push("World")
        self.assertEqual(self.my_stack.peek(), "World")

    def test_size(self):
        self.my_stack.push("Hello")
        self.my_stack.push("World")
        self.assertEqual(self.my_stack.size(), 2)

    def test_print(self):
        self.my_stack.push("Hello")
        self.my_stack.push("World")
        self.assertEqual(self.my_stack.print_all_items(), "Hello, World")
