import unittest
from main import RBTree, Node, RED


class RBTreeTest(unittest.TestCase):
    def test_delete(self):
        rb_tree = RBTree()
        node1 = Node(data=1, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node34 = Node(data=34, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node64 = Node(data=64, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node12 = Node(data=12, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node49 = Node(data=49, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node29 = Node(data=29, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node68 = Node(data=68, left=rb_tree.nil, right=rb_tree.nil, color=RED)

        rb_tree.insert(node1)
        rb_tree.insert(node34)
        rb_tree.insert(node64)
        rb_tree.insert(node12)
        rb_tree.insert(node49)
        rb_tree.insert(node29)
        rb_tree.insert(node68)

        self.assertEqual(rb_tree.delete(node12), (0, 1))

    def test_insert(self):
        rb_tree = RBTree()
        node6 = Node(data=6, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node7 = Node(data=7, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node34 = Node(data=34, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node75 = Node(data=75, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node23 = Node(data=23, left=rb_tree.nil, right=rb_tree.nil, color=RED)

        rb_tree.insert(node6)
        rb_tree.insert(node7)
        rb_tree.insert(node23)
        rb_tree.insert(node75)

        self.assertEqual((2, 1), rb_tree.insert(node34))

    def test_get_parent(self):
        rb_tree = RBTree()
        node6 = Node(data=6, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node7 = Node(data=7, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node34 = Node(data=34, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node75 = Node(data=75, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node23 = Node(data=23, left=rb_tree.nil, right=rb_tree.nil, color=RED)

        rb_tree.insert(node6)
        rb_tree.insert(node7)
        rb_tree.insert(node23)
        rb_tree.insert(node75)
        rb_tree.insert(node34)

        self.assertEqual(node23, rb_tree.get_parent_node(node34))

    def test_get_child(self):
        rb_tree = RBTree()
        node1 = Node(data=1, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node34 = Node(data=34, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node64 = Node(data=64, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node12 = Node(data=12, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node49 = Node(data=49, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node29 = Node(data=29, left=rb_tree.nil, right=rb_tree.nil, color=RED)
        node68 = Node(data=68, left=rb_tree.nil, right=rb_tree.nil, color=RED)

        rb_tree.insert(node1)
        rb_tree.insert(node34)
        rb_tree.insert(node64)
        rb_tree.insert(node12)
        rb_tree.insert(node49)
        rb_tree.insert(node29)
        rb_tree.insert(node68)

        self.assertEqual(node29, rb_tree.get_child_node(node12))


if __name__ == '__main__':
    unittest.main()
