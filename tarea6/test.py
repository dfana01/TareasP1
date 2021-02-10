import unittest
from double_linked_list import DoubleLinkedList, Node
from stack import Stack


SAMPLE_DOUBLE_LINKED_LIST = DoubleLinkedList()
SAMPLE_DOUBLE_LINKED_LIST.add_all(Node(1), Node(2), Node(3), Node(4), Node(5))


class TestDoubleLinkedList(unittest.TestCase):
    def test_add(self):
        list_copy = SAMPLE_DOUBLE_LINKED_LIST.clone()
        list_copy.add(Node(33))
        self.assertEqual(list_copy.size, 6)

    def test_add_index(self):
        list_copy = SAMPLE_DOUBLE_LINKED_LIST.clone()
        node = Node(33)
        list_copy.add_index(3, node)
        self.assertEqual(list_copy.get(3), node)

    def test_index_empty(self):
        self.assertEqual(DoubleLinkedList().index(Node(1)), None)

    def test_str(self):
        ddl = DoubleLinkedList()
        ddl.add_all(Node(1), Node(2))
        self.assertEqual(str(ddl), "[1,2]")

    def test_add_all(self):
        dll = DoubleLinkedList()
        dll.add_all(Node(1), Node(2), Node(3))
        self.assertEqual(dll.size, 3)

    def test_clear(self):
        list_copy = SAMPLE_DOUBLE_LINKED_LIST.clone()
        list_copy.clear()
        self.assertEqual(list_copy.size, 0)

    def test_clone(self):
        list_copy = SAMPLE_DOUBLE_LINKED_LIST.clone()
        self.assertTrue(list_copy != SAMPLE_DOUBLE_LINKED_LIST)

    def test_contains(self):
        self.assertTrue(Node(1) in SAMPLE_DOUBLE_LINKED_LIST)

    def test_get(self):
        list_copy = SAMPLE_DOUBLE_LINKED_LIST.clone()
        node = Node(1)
        list_copy.add_index(1, node)
        self.assertTrue(list_copy.get(1) == node)

    def test_remove(self):
        list_copy = SAMPLE_DOUBLE_LINKED_LIST.clone()
        list_copy.remove(1)
        self.assertTrue(list_copy.size < SAMPLE_DOUBLE_LINKED_LIST.size)

    def test_index(self):
        list_copy = SAMPLE_DOUBLE_LINKED_LIST.clone()
        node = Node(55)
        list_copy.add_index(1, node)
        self.assertTrue(list_copy.index(node) == 1)

    def test_iter(self):
        for _ in SAMPLE_DOUBLE_LINKED_LIST:
            self.assertTrue(True)
            break


class TestStack(unittest.TestCase):
    def test_is_empty(self):
        stack = Stack()
        stack.push(Node(3))
        self.assertTrue(not stack.is_empty())

    def test_peek(self):
        stack = Stack()
        stack.push(Node(1))
        stack.push(Node(2))
        stack.push(Node(3))
        node = Node(4)
        stack.push(node)
        self.assertEqual(stack.peek(), node)

    def test_pop(self):
        stack = Stack()
        stack.push(Node(1))
        stack.push(Node(2))
        node = Node(3)
        stack.push(node)
        stack.push(Node(4))
        stack.pop()
        self.assertEqual(stack.peek(), node)

    def test_push(self):
        stack = Stack()
        stack.push(Node(3))
        self.assertTrue(not stack.is_empty())

    def test_search(self):
        stack = Stack()
        stack.push(Node(1))
        stack.push(Node(2))
        node = Node(3)
        stack.push(Node(3))
        self.assertEqual(stack.search(node), 3)


if __name__ == '__main__':
    unittest.main()
