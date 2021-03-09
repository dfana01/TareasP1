"""

"""

class Student:
    display_name = None
    academic_index = 0
    age = 0

    def __init__(self, display_name, academic_index, age):
        self.display_name = display_name
        self.academic_index = academic_index
        self.age = age

    def __gt__(self, other):
        return self.age > other.age and self.academic_index > other.academic_index

    def __lt__(self, other):
        return self.age < other.age and self.academic_index < other.academic_index

    def __eq__(self, other):
        return self.age == other.age and self.academic_index == other.academic_index

    def __str__(self):
        return f"{self.display_name}, {self.age}, {self.academic_index}"

    def __repr__(self):
        return f"{self.display_name}, {self.academic_index}, {self.age}"


class HeapMax:
    def __init__(self):
        self.elements = []
        self.size = 0

    @staticmethod
    def parent(i):
        """
        :complexity
             :space: O(1), solo hace un calculo matematico
             :time: O(1), solo hace un calculo matematico
        """
        return i // 2

    @staticmethod
    def left(i):
        """
        :complexity
             :space: O(1), solo hace un calculo matematico
             :time: O(1), solo hace un calculo matematico
        """
        return 2 * i + 1

    @staticmethod
    def right(i):
        """
        :complexity
             :space: O(1), solo hace un calculo matematico
             :time: O(1), solo hace un calculo matematico
        """
        return 2 * i + 2

    def insert(self, val):
        """
        :complexity
             :space: O(1), dado que solo ingresa
            :time: O(lg n), pues utiliza la complejidad de increase_key
        """
        self.elements.append(val)
        self.size = len(self.elements)
        self.increase_key(self.elements, self.size - 1)

    def increase_key(self, arr, i):
        """
        :complexity
             :space: O(1), dado que solo usa variables especificas, eso no tomando en cuenta la llamada de stack
             :time: O(lg n), pues recorre las raices de los subarboles
        """
        while arr[i] > arr[self.parent(i)]:
            arr[i], arr[self.parent(i)] = arr[self.parent(i)], arr[i]
            i = self.parent(i)

    def heapify(self, arr, n, i):
        """
        :complexity
             :space: O(1), dado que solo usa variables especificas, eso no tomando en cuenta la llamada de stack
             :time: O(lg n), pues recorre el arbol recursivamente
        """
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def build(self, elements):
        """
        :complexity
             :space: O(1), dado que solo usa la misma lista
             :time: O(n), pues recorre todos los elementos
        """
        self.elements = elements
        self.size = len(elements)
        for i in range(self.size//2 - 1, -1, -1):
            self.heapify(self.elements, self.size, i)

    def maximum(self):
        """
        :complexity
             :space: O(1), dado que solo ingresa
             :time: O(1), dado que solo se saca el primer elemento del arreglo
        """
        if len(self.elements) >= 1:
            return self.elements[0]
        else:
            return None

    def extract_max(self):
        """
        :complexity
             :space: O(1), dado que solo usa variables
             :time: O(lg n), ya que usa heapify
        """
        if len(self.elements) < 1:
            raise Exception("Heap underflow")
        max_el = self.maximum()
        self.elements[0] = self.elements.pop()
        self.size = len(self.elements)
        self.heapify(self.elements, self.size, 0)
        return max_el


class HeapMin:
    def __init__(self):
        self.elements = []
        self.size = 0

    @staticmethod
    def parent(i):
        """
        :complexity
             :space: O(1), solo hace un calculo matematico
             :time: O(1), solo hace un calculo matematico
        """
        return i // 2

    @staticmethod
    def left(i):
        """
        :complexity
             :space: O(1), solo hace un calculo matematico
             :time: O(1), solo hace un calculo matematico
        """
        return 2 * i + 1

    @staticmethod
    def right(i):
        """
        :complexity
             :space: O(1), solo hace un calculo matematico
             :time: O(1), solo hace un calculo matematico
        """
        return 2 * i + 2

    def insert(self, val):
        """
        :complexity
             :space: O(1), dado que solo ingresa
            :time: O(lg n), pues utiliza la complejidad de decrease_key
        """
        self.elements.append(val)
        self.size = len(self.elements)
        self.decrease_key(self.elements, self.size - 1)

    def decrease_key(self, arr, i):
        """
        :complexity
             :space: O(1), dado que solo usa variables especificas, eso no tomando en cuenta la llamada de stack
             :time: O(lg n), pues recorre las raices de los subarboles
        """
        while arr[i] < arr[self.parent(i)]:
            arr[i], arr[self.parent(i)] = arr[self.parent(i)], arr[i]
            i = self.parent(i)

    def heapify(self, arr, n, i):
        """
        :complexity
             :space: O(1), dado que solo usa variables especificas, eso no tomando en cuenta la llamada de stack
             :time: O(lg n), pues recorre el arbol recursivamente
        """
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < n and arr[left] < arr[largest]:
            largest = left

        if right < n and arr[right] < arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def build(self, elements):
        """
        :complexity
             :space: O(1), dado que solo usa la misma lista
             :time: O(n), pues recorre todos los elementos
        """
        self.elements = elements
        self.size = len(elements)
        for i in range(self.size//2 - 1, -1, -1):
            self.heapify(self.elements, self.size, i)

    def minimum(self):
        """
        :complexity
             :space: O(1), dado que solo ingresa
             :time: O(1), dado que solo se saca el primer elemento del arreglo
        """
        if len(self.elements) >= 1:
            return self.elements[0]
        else:
            return None

    def extract_min(self):
        """
        :complexity
             :space: O(1), dado que solo usa variables
             :time: O(lg n), ya que usa heapify
        """
        if len(self.elements) < 1:
            raise Exception("Heap underflow")
        max_el = self.minimum()
        self.elements[0] = self.elements.pop()
        self.size = len(self.elements)
        self.heapify(self.elements, self.size, 0)
        return max_el


def heap_sort(head_class, elements):
    """
    :complexity
         :space: O(1), dado que no es usa otra lista.
         :time: O(n lg n), pues build element es de O(n) y el heapify toma O(lg n)
    """
    heap = head_class()
    heap.build(elements)
    for i in range(len(elements) - 1, 0, -1):
        heap.elements[0], heap.elements[i] = heap.elements[i], heap.elements[0]
        heap.heapify(elements, i, 0)
    return heap.elements
