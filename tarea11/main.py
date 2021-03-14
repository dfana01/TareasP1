from math import comb

NUMBER_OF_LETTER = 26
LETTER_TYPE = 2
KEY_SIZE = 5


class Element:
    data = None
    prev = None
    next = None

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return "{}".format(self.data)

    def __hash__(self):
        """
        :complexity
             :space: O(n), recorremos todo el tamaño del string
             :time: O(1), solo usamos una variable
        """
        n = 0
        for ch in self.data:
            n += ord(ch)
        return n


class DirectAddressTable:
    def __init__(self):
        size = comb(NUMBER_OF_LETTER * LETTER_TYPE, KEY_SIZE) + 1
        self.elements = [None for _ in range(size)]

    def search(self, val):
        """
        :complexity
             :space: O(1), dado que usamos variables extra pero son constantes
             :time: O(n), dado que recorremos la lista cuando necesitamos buscar una variable
        """
        element = Element(val)
        key = hash(element)
        key_elements: DoubleLinkedList = self.elements[key]
        if key_elements is not None:
            el = key_elements.get(element)
            if el is not None:
                return el.data
            return key_elements.get(element)
        else:
            return None

    def insert(self, val):
        """
        :complexity
             :space: O(1), dado que usamos variables extra pero son constantes
             :time: O(1), dado que no recorremos la lista para agregar
        """
        if not val.isalpha():
            raise Exception("The key needs to compose all by letters")
        if len(val) != 5:
            raise Exception("Key need to be 5 letter")

        element = Element(val)
        key = hash(element)

        key_elements: DoubleLinkedList = self.elements[key]
        if key_elements is None:
            key_elements = DoubleLinkedList()
        key_elements.add(element)

        self.elements[key] = key_elements

    def delete(self, val):
        """
        :complexity
             :space: O(1), dado que usamos variables extra pero son constantes
             :time: O(n), dado que recorremos la lista para eliminar
        """
        element = Element(val)
        key = hash(element)
        key_elements: DoubleLinkedList = self.elements[key]
        if key_elements is not None:
            key_elements.remove(key_elements.get(element))
        else:
            return None


class DoubleLinkedList:
    nil: Element
    current: Element
    size: 0

    def __init__(self):
        self.nil = Element(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil
        self.current = self.nil.next
        self.size = 0

    def add(self, element: Element):
        """
        :complexity
             :space: O(1), para agregar vemos que la complejidad es O(1) siendo el tiempo constantes.
             :time: O(1), dado que no usamos ninguna variable extra.
        """
        element.next = self.nil.next
        self.nil.next.prev = element
        self.nil.next = element
        element.prev = self.nil
        self.size += 1

    def get(self, el0: Element):
        """
        :complexity
             :space: O(1), No se usan variables extra
             :time: O(n), dado que recorremos la lista completa
        """
        for el1 in self:
            if el1.data == el0.data:
                return el1
        return None

    def remove(self, element: Element):
        """
        :complexity
             :space: O(1), No se usan variables extra
             :time: O(1), Dado que solo removemos las referencia
        """
        element.prev.next = element.next
        element.next.prev = element.prev
        self.size -= 1

    def __iter__(self):
        self.current = self.nil.prev
        return self

    def __next__(self):
        if self.current != self.nil:
            element = self.current
            self.current = self.current.prev
            return element
        raise StopIteration

    def __str__(self):
        return "[{}]".format(",".join([str(n.data) for n in self]))

