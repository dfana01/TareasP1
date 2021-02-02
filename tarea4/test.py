import unittest
from main import bubble_sort, insertion_sort, selection_sort, Student, get_shuffle_list

SORT_LIST = [
    Student("Antony"),
    Student("Erin"),
    Student("Hannah"),
    Student("Ilyas"),
    Student("Maciej"),
    Student("Maximillian"),
    Student("Monet"),
    Student("Reema"),
    Student("Rhiannan"),
    Student("Travis")
]


class SortTest(unittest.TestCase):
    def test_bubble_sort_clear(self):
        self.assertEqual(",".join([s.display_name for s in SORT_LIST]),
                         ",".join(bubble_sort([s.display_name for s in get_shuffle_list()])))

    def test_insertion_sort_clear(self):
        self.assertEqual(",".join([s.display_name for s in SORT_LIST]),
                         ",".join(insertion_sort([s.display_name for s in get_shuffle_list()])))

    def test_selection_sort_clear(self):
        self.assertEqual(",".join([s.display_name for s in SORT_LIST]),
                         ",".join(selection_sort([s.display_name for s in get_shuffle_list()])))


if __name__ == '__main__':
    unittest.main()
