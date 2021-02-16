from main import poisonous_plants, minimum_bribes, has_cycle
from linked_list import LinkedList
import unittest


class Test(unittest.TestCase):
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

    def test_case_1_poisonous_plants(self):
        self.assertEqual(poisonous_plants([6, 5, 8, 4, 7, 10, 9]), 2)

    def test_case_2_poisonous_plants(self):
        self.assertEqual(poisonous_plants([3, 2, 5, 4]), 2)

    def test_case_3_poisonous_plants(self):
        self.assertEqual(poisonous_plants([4, 3, 7, 5, 6, 4, 2]), 3)

    def test_case_1_minimum_bribes(self):
        self.assertEqual(minimum_bribes([2, 1, 5, 3, 4]), 3)

    def test_case_2_minimum_bribes(self):
        self.assertEqual(minimum_bribes([2, 5, 1, 3, 4]), "Too chaotic")

    def test_case_3_minimum_bribes(self):
        self.assertEqual(minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4]), 7)

    def test_case_4_minimum_bribes(self):
        self.assertEqual(minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4]), "Too chaotic")


if __name__ == '__main__':
    unittest.main()
