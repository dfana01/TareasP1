class Node:
    data = None
    prev = None
    next = None

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return "{}".format(self.data)


class DoubleLinkedList:
    nil: Node
    current: Node
    size: 0

    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil
        self.current = self.nil.next
        self.size = 0

    def add(self, node: Node):
        node.next = self.nil.next
        self.nil.next.prev = node
        self.nil.next = node
        node.prev = self.nil
        self.size += 1

    def add_index(self, index: int, node: Node):
        assert index <= self.size, "Index out of bounds"
        node0 = self.get(index - 1) if index > 1 else self.nil
        node.prev = node0.prev
        node.next = node0
        node0.prev.next = node
        node0.prev = node
        self.size += 1

    def add_all(self, *nodes):
        for node in nodes:
            self.add(node)

    def clear(self):
        self.nil.next = self.nil
        self.nil.prev = self.nil
        self.size = 0

    def clone(self):
        copy = type(self)()
        for node in self:
            copy.add(type(node)(node.data))
        return copy

    def __contains__(self, node: Node):
        return self.index(node)

    def get(self, index: int):
        for index0, node in enumerate(self):
            if (index - 1) == index0:
                return node

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove(self, index: int):
        self._remove(self.get(index))

    def index(self, node: Node):
        for index, node0 in enumerate(self):
            if node.data == node0.data:
                return index + 1
        return None

    def __iter__(self):
        self.current = self.nil.prev
        return self

    def __next__(self):
        if self.current != self.nil:
            node = self.current
            self.current = self.current.prev
            return node
        raise StopIteration

    def __str__(self):
        return "[{}]".format(",".join([str(n.data) for n in self]))
