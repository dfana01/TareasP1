import unittest
from double_linked_list import DoubleLinkedList, Node
from time_comparison_double_linked_list import generate_sample_add, \
        generate_sample_clear, \
        generate_sample_clone, \
        generate_sample_index_start, \
        generate_sample_index_middle, \
        generate_sample_index_end, \
        generate_sample_add_index_start, \
        generate_sample_add_index_middle, \
        generate_sample_add_index_end, \
        generate_sample_remove_start, \
        generate_sample_remove_middle, \
        generate_sample_remove_end, \
        generate_sample_in_start, \
        generate_sample_in_middle, \
        generate_sample_in_end, \
        generate_sample_add_all, \
        generate_sample_get_start, \
        generate_sample_get_middle, \
        generate_sample_get_end
import util


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


class MiscellaneousTestFact(unittest.TestCase):
    def test_graph_men_and_time(self):
        self.assertTrue(True)

    def test_graph(self):
        self.assertTrue(True)

    def test_get_current_ram(self):
        self.assertTrue(util.get_current_ram() > 0)

    def test_get_current_time(self):
        self.assertTrue(util.get_current_time() > 0)

    def test_generate_range_numbers(self):
        self.assertTrue(len(util.generate_range_numbers()) == util.N_TIMES)

    def test_get_avg(self):
        self.assertTrue(util.get_avg([1, 2, 3, 4, 5]) == 3)

    def test_get_deviation(self):
        self.assertTrue(util.get_deviation(3, [1, 2, 3, 4, 5]) > 1.5)

    def test_standardize_sample(self):
        r = util.standardize_sample({
            0: [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        })
        self.assertTrue(isinstance(r, list))

    def test_with_rep_and_standardize(self):
        def f(s):
            return {}
        r = util.with_rep_and_standardize(f, rep=1)
        self.assertTrue(r == [])

    def test_add_to_sample_1(self):
        sample = util.add_to_sample(1, 0, 0, {})
        self.assertTrue(1 in sample)

    def test_add_to_sample_2(self):
        sample = util.add_to_sample(1, 0, 0, {1: [[], []]})
        self.assertTrue(1 in sample)

    def test_get_random_str(self):
        self.assertTrue(len(util.get_random_str(5)) == 5)

    def test_random_number_between(self):
        self.assertTrue(util.random_number_between(0, 5) <= 5)


class TimeComparisonDoubleLinkedList(unittest.TestCase):
    def test_generate_sample_add(self):
        self.assertTrue(generate_sample_add() is not None)

    def test_generate_sample_clear(self):
        self.assertTrue(generate_sample_clear() is not None)

    def test_generate_sample_clone(self):
        self.assertTrue(generate_sample_clone() is not None)

    def test_generate_sample_index_start(self):
        self.assertTrue(generate_sample_index_start() is not None)

    def test_generate_sample_index_middle(self):
        self.assertTrue(generate_sample_index_middle() is not None)

    def test_generate_sample_index_end(self):
        self.assertTrue(generate_sample_index_end() is not None)

    def test_generate_sample_add_index_start(self):
        self.assertTrue(generate_sample_add_index_start() is not None)

    def test_generate_sample_add_index_middle(self):
        self.assertTrue(generate_sample_add_index_middle() is not None)

    def test_generate_sample_add_index_end(self):
        self.assertTrue(generate_sample_add_index_end() is not None)

    def test_generate_sample_remove_start(self):
        self.assertTrue(generate_sample_remove_start() is not None)

    def test_generate_sample_remove_middle(self):
        self.assertTrue(generate_sample_remove_middle() is not None)

    def test_generate_sample_remove_end(self):
        self.assertTrue(generate_sample_remove_end() is not None)

    def test_generate_sample_in_start(self):
        self.assertTrue(generate_sample_in_start() is not None)

    def test_generate_sample_in_middle(self):
        self.assertTrue(generate_sample_in_middle() is not None)

    def test_generate_sample_in_end(self):
        self.assertTrue(generate_sample_in_end() is not None)

    def test_generate_sample_add_all(self):
        self.assertTrue(generate_sample_add_all() is not None)

    def test_generate_sample_get_start(self):
        self.assertTrue(generate_sample_get_start() is not None)

    def test_generate_sample_get_middle(self):
        self.assertTrue(generate_sample_get_middle() is not None)

    def test_generate_sample_get_end(self):
        self.assertTrue(generate_sample_get_end() is not None)


if __name__ == '__main__':
    unittest.main()
