"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
"""


class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = Node(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def has_cycle(head):
    node1 = head
    node2 = head.next
    while node2 is not None and node2.next is not None:
        if node1 == node2:
            return 1
        node1 = node1.next
        node2 = node2.next.next
    return 0