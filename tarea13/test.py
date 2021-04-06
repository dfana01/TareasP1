import unittest
from main import inorder, preorder, postorder, infix_to_postfix, generate_tree

tree = generate_tree(infix_to_postfix("(a+b)*(c-e)+(f+(g*h))-i"))


class TTreeTest(unittest.TestCase):
    def test_polish_notation(self):
        self.assertEqual('ab+ce-*fgh*++i-', postorder(tree))

    def test_reverse_polish_notation(self):
        self.assertEqual('-+*+ab-ce+f*ghi', preorder(tree))

    def test_infix(self):
        self.assertEqual('a+b*c-e+f+g*h-i', inorder(tree))


if __name__ == '__main__':
    unittest.main()
