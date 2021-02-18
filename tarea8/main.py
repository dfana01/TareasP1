class Student:
    display_name = None

    def __init__(self, display_name):
        self.display_name = display_name

    def __gt__(self, other):
        return self.display_name > other.display_name

    def __lt__(self, other):
        return self.display_name < other.display_name

    def __eq__(self, other):
        return self.display_name == other.display_name


def binary_search(students, min_idx, max_idx, student):
    """
    :complexity
        - Time: la complejidad de tiempo
        - Space
    """
    if min_idx <= max_idx:
        mid_idx = (min_idx + max_idx) // 2
        if students[mid_idx] == student:
            return students[mid_idx]
        elif students[mid_idx] > student:
            return binary_search(students, min_idx, mid_idx - 1, student)
        else:
            return binary_search(students, mid_idx + 1, max_idx, student)
    else:
        return None
