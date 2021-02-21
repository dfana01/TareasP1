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
        - Time: O(log n), este algoritmos es de esta complejidad dada que nunca se recorre el arreglo completo este
            sobre entiende que el mismo esta organizado y divide entre dos la cantidad de posiciones que recorrerá
            cada vez que se llama a la función.
        - Space: O(1), Como solo usamos una variable extra y no prestamos atención a los recursos consumido por la
            llamada recursivas decimos que el costo de espacio es constante.
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
