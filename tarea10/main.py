from datetime import datetime, timedelta
from time import time

class Mail:
    epoch = 0

    def __init__(self, epoch):
        self.epoch = epoch

    def __gt__(self, other):
        return (self.epoch * -1) > (other.epoch * -1)

    def __lt__(self, other):
        return (self.epoch * -1) < (other.epoch * -1)

    def __eq__(self, other):
        return (self.epoch * -1) == (other.epoch * -1)

    def __str__(self):
        return f"{self.epoch}"

    def __repr__(self):
        return f"{self.epoch}"


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


class MailerHandler:
    def __init__(self):
        self.heap = HeapMax()

    def queue(self, mail):
        """
        :complexity
             :space: O(1), dado que solo ingresa el mail
            :time: O(lg n), pues utiliza la complejidad de insert
        """
        self.heap.insert(mail)

    def dequeue(self):
        """
        :complexity
             :space: O(1), dado que no se usa variables
             :time: O(lg n), ya que se usa extract max y se hereda la complejidad
        """
        return self.heap.extract_max()


def get_epoch(days=1):
    date = datetime.fromtimestamp(int(time())) + timedelta(days=days)
    return int(date.timestamp())
