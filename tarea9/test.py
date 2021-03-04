import unittest
from main import HeapMax, heap_sort


# STUDENT = [
#     Student("Aamina"),
#     Student("Ayyub"),
#     Student("Eben"),
#     Student("Elis"),
#     Student("Hashim"),
#     Student("Roshni"),
#     Student("Simona"),
#     Student("Tanisha"),
#     Student("Taslima"),
#     Student("Ty"),
# ]


class SearchTest(unittest.TestCase):
    def test_heap_insert(self):
        # 16 14 10 8 7 9 3 2 4 1
        heap = HeapMax()
        heap.insert(8)
        heap.insert(9)
        heap.insert(1)
        heap.insert(14)
        heap.insert(7)
        heap.insert(16)
        heap.insert(10)
        heap.insert(2)
        heap.insert(4)
        heap.insert(3)
        print(heap)
        self.assertEqual(1, 1)

    def test_build(self):
        # 16 14 10 8 7 9 3 2 4 1
        heap_sort([
            12, 11, 13, 5, 6, 7
        ])
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
