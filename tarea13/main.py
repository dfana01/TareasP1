
OPERATORS = {'+', '-', '*', '/', '(', ')'}
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}


class TTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def infix_to_postfix(exp):
    stack = []
    output = []
    for ch in exp:
        if ch not in OPERATORS:
            output.append(ch)
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and \
                    stack[-1] != '(' \
                    and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())
    return output


def generate_tree(postfix):
    stack = []
    for char in postfix:
        if char not in OPERATORS:
            t = TTree(char)
            stack.append(t)
        else:
            t = TTree(char)
            t1 = stack.pop()
            t2 = stack.pop()
            t.right = t1
            t.left = t2
            stack.append(t)
    t = stack.pop()
    return t


def inorder(t):
    output = ""
    if t is not None:
        output += inorder(t.left) + t.value + inorder(t.right)
    return output


def postorder(root):
    output = ""
    if root:
        output += postorder(root.left) + postorder(root.right) + root.value
    return output


def preorder(root):
    output = ""
    if root:
        output += root.value + preorder(root.left) + preorder(root.right)
    return output
