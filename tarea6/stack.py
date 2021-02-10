
from double_linked_list import DoubleLinkedList


class Stack(DoubleLinkedList):
    def __init__(self):
        super().__init__()

    """
    Dado que utilizamos un elemento para ver cuando la misma esta vacia este algorimo tiene una complejidad de O(1)
    """
    def is_empty(self):
        return self.size == 0

    """
    Dado que utilizamos el elemento sentinela para el proximo elemento tiene una complejidad O(1)
    """
    def peek(self):
        assert not self.is_empty(), "underflow"
        return self.nil.next

    """
    Dado que utilizamos el metodo remove de la lista que tiene una complejidad de O(1) este tambien tendra la misma complejidad
    """
    def pop(self):
        assert not self.is_empty(), "underflow"
        self.size -= 1
        element = self.peek()
        self._remove(element)
        return element

    """
    Dado que utilizamos el metodo add de la lista que tiene una complejidad de O(1) este tambien tendra la misma complejidad
    """
    def push(self, element):
        self.add(element)
        self.size += 1

    """
    Dado que utilizamos el metodo index de la lista que tiene una complejidad de O(n) este tambien tendra la misma complejidad
    """
    def search(self, element):
        return self.index(element)
