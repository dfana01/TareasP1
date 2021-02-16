import unittest

from problems.has_cycle import LinkedList, has_cycle


class HasCycleTest(unittest.TestCase):
    def test_case_1_has_cycle(self):
        ll = LinkedList()
        ll.insert_node(1)
        ll.insert_node(2)
        ll.insert_node(3)
        ll.head.next.next.next = ll.head.next
        self.assertEqual(1, has_cycle(ll.head))

    def test_case_2_has_cycle(self):
        ll = LinkedList()
        ll.insert_node(1)
        ll.insert_node(2)
        ll.insert_node(3)
        self.assertEqual(0, has_cycle(ll.head))


if __name__ == '__main__':
    unittest.main()
