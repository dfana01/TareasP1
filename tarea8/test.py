import unittest
from main import binary_search, Student

STUDENT = [
    Student("Aamina"),
    Student("Ayyub"),
    Student("Eben"),
    Student("Elis"),
    Student("Hashim"),
    Student("Roshni"),
    Student("Simona"),
    Student("Tanisha"),
    Student("Taslima"),
    Student("Ty"),
]


class SearchTest(unittest.TestCase):
    def test_binary_middle(self):
        self.assertEqual(binary_search(STUDENT, 0, len(STUDENT)-1, Student("Roshni")),
                         Student("Roshni"))

    def test_binary_top(self):
        self.assertEqual(binary_search(STUDENT, 0, len(STUDENT)-1, Student("Ty")),
                         Student("Ty"))

    def test_binary_bottom(self):
        self.assertEqual(binary_search(STUDENT, 0, len(STUDENT)-1, Student("Aamina")),
                         Student("Aamina"))

    def test_binary_not_found(self):
        self.assertEqual(binary_search(STUDENT, 0, len(STUDENT)-1, Student("Dante")),
                         None)


if __name__ == '__main__':
    unittest.main()
