import unittest
from main import HeapMax, HeapMin, heap_sort, Student

STUDENTS = [
    Student("Aamina", 4.0, 19),
    Student("Ayyub", 3.7, 17),
    Student("Eben", 2.3, 21),
    Student("Elis", 3.2, 28),
    Student("Zeta", 1.4, 29),
    Student("Hashim", 3.6, 23),
    Student("Roshni", 2.1, 36),
    Student("Simona", 3.4, 33),
    Student("Tanisha", 1.6, 23),
    Student("Taslima", 3.1, 18),
    Student("Ty", 3.0, 20)
]

STUDENTS_ORDERS_MIN = [
    Student("Aamina", 4.0, 19),
    Student("Simona", 3.4, 33),
    Student("Tanisha",  1.6, 23),
    Student("Zeta",  1.4, 29),
    Student("Hashim", 3.6, 23),
    Student("Roshni", 2.1, 36),
    Student("Elis", 3.2, 28),
    Student("Eben", 2.3, 21),
    Student("Taslima", 3.1, 18),
    Student("Ty", 3.0, 20),
    Student("Ayyub", 3.7, 17)
]

STUDENTS_ORDERS_MAX = [
    Student("Ayyub", 3.7, 17),
    Student("Ty", 3.0, 20),
    Student("Simona", 3.4, 33),
    Student("Zeta", 1.4, 29),
    Student("Eben", 2.3, 21),
    Student("Roshni", 2.1, 36),
    Student("Elis", 3.2, 28),
    Student("Tanisha", 1.6, 23),
    Student("Taslima", 3.1, 18),
    Student("Hashim", 3.6, 23),
    Student("Aamina", 4.0, 19),
]


class HeapTest(unittest.TestCase):
    def test_heap_max_insert(self):
        heap = HeapMax()
        heap.insert(Student("Aamina", 4.0, 19))
        heap.insert(Student("Ayyub", 3.7, 17))
        heap.insert(Student("Eben", 2.3, 21))
        heap.insert(Student("Elis", 3.2, 28))
        heap.insert(Student("Zeta", 1.4, 29))
        heap.insert(Student("Hashim", 3.6, 23))
        heap.insert(Student("Roshni", 2.1, 36))
        heap.insert(Student("Simona", 3.4, 33))
        heap.insert(Student("Tanisha", 1.6, 23))
        heap.insert(Student("Taslima", 3.1, 18))
        heap.insert(Student("Ty", 3.0, 20))
        self.assertEqual(heap.extract_max(), Student("Aamina", 4.0, 19))

    def test_heap_min_insert(self):
        heap = HeapMin()
        heap.insert(Student("Aamina", 4.0, 19))
        heap.insert(Student("Ayyub", 3.7, 17))
        heap.insert(Student("Eben", 2.3, 21))
        heap.insert(Student("Elis", 3.2, 28))
        heap.insert(Student("Zeta", 1.4, 29))
        heap.insert(Student("Hashim", 3.6, 23))
        heap.insert(Student("Roshni", 2.1, 36))
        heap.insert(Student("Simona", 3.4, 33))
        heap.insert(Student("Tanisha", 1.6, 23))
        heap.insert(Student("Taslima", 3.1, 18))
        heap.insert(Student("Ty", 3.0, 20))
        self.assertEqual(heap.extract_min(), Student("Ayyub", 3.7, 17))

    def test_heap_build(self):
        heap = HeapMax()
        heap.build([17, 2, 1, 7, 3, 19, 36, 25, 100])
        self.assertEqual(heap.extract_max(), 100)

    def test_heapsort_max(self):
        r = heap_sort(HeapMax, STUDENTS.copy())
        self.assertEqual(r, STUDENTS_ORDERS_MAX)

    def test_heapsort_min(self):
        r = heap_sort(HeapMin, STUDENTS.copy())
        self.assertEqual(r, STUDENTS_ORDERS_MIN)


if __name__ == '__main__':
    unittest.main()
