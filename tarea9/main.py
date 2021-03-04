
"""
Tarea9

• Implementar el algoritmo de heapsort (ascendente y descedente) para un arreglo/lista de estudiantes

• Ordenar por índice académico y por edad.

• Incluye MAX-HEAPIFY[]
          MAX-HEAP-INSERT[]
          HEAP-INCREASE-KEY[]
          BUILD-MAX-HEAP[]
          HEAP-MAXIMUM[]
          HEAP-EXTRACT-MAX[*]

          MIN-HEAPIFY[*]
          BUILD-MIN-HEAP[*]

• Agregar en el docstring la complejidad temporal y espacial de cada método

• Indicar (en comentario) complejidad de tiempo y de espacio de la solución

• Incluir unit test
"""


class HeapMax:
    def __init__(self):
        self.elements = [0]
        self.elements[0] = float('inf')
        self.size = 0

    @staticmethod
    def parent(i):
        return i // 2

    @staticmethod
    def left(i):
        return 2 * i

    @staticmethod
    def right(i):
        return (2 * i) + 1

    def insert(self, key):
        self.size += 1
        self.elements.append(float('-inf'))
        self.increase_key(key)

    def increase_key(self, key):
        i = self.size
        if key < self.elements[i]:
            raise Exception("New key is smaller than current key")
        self.elements[i] = key
        while i > 1 and self.elements[self.parent(i)] < self.elements[i]:
            self.elements[self.parent(i)], self.elements[i] = self.elements[i], self.elements[self.parent(i)]
            i = self.parent(i)

    def heapify(self, i):
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < self.size and self.elements[left] > self.elements[largest]:
            largest = left

        if right < self.size and self.elements[right] > self.elements[largest]:
            largest = right

        if largest != i:
            self.elements[i], self.elements[largest] = self.elements[largest], self.elements[i]
            self.heapify(largest)

    def build(self, elements):
        self.elements = [0] + elements
        self.elements[0] = float('inf')
        self.size = len(elements) - 1
        for i in range(self.size//2, 1, -1):
            self.heapify(i)

    def maximum(self):
        if len(self.elements) >= 1:
            return self.elements[1]
        else:
            return None

    def extract_max(self):
        if self.elements[self.size] < 1:
            raise Exception("Heap underflow")
        max_el = self.maximum()
        self.elements[1] = self.elements[self.size]
        self.size = self.size - 1
        self.heapify(1)
        return max_el

    def __str__(self):
        return ",".join(map(str, self.elements[1:]))


def heap_sort(elements):
    heap = HeapMax()
    heap.build(elements)
    for i in range(heap.size, 2, -1):
        heap.elements[1], heap.elements[i] = heap.elements[i], heap.elements[1]
        heap.heapify(i)
    print(heap)
