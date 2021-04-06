BLACK = 0
RED = 1


class Node:
    def __init__(self, data=0, parent=None, left=None, right=None, color=RED):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class RBTree:
    def __init__(self):
        self.root = self.nil = Node(color=BLACK)

    def insert(self, z):
        y = None
        x = self.root
        while x != self.nil:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        return self.insert_fix_up(z)

    def delete(self, z):
        color_changes_count = 0
        fix_delete_counts = (0,0)
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            color_changes_count += 1
        if y_original_color == BLACK:
            fix_delete_counts = self.fix_delete(x)
        return fix_delete_counts[0], fix_delete_counts[1] + color_changes_count

    def get_parent_node(self, x):
        if x.left != self.nil:
            return self.maximum(x.left)
        y = x.parent
        while y != self.nil and x == y.left:
            x = y
            y = y.parent
        return y

    def get_child_node(self, x):
        if x.right != self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def insert_fix_up(self, z):
        color_changes_count = 0
        rotation_count = 0
        if z.parent is None:
            z.color = BLACK
            return
        if z.parent.parent is None:
            return
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    y.color = BLACK
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                    color_changes_count += 1
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                        rotation_count += 1
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
                    rotation_count += 1
                    color_changes_count += 1
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                    color_changes_count += 1
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                        rotation_count += 1
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)
                    rotation_count += 1
                    color_changes_count += 1
            if z == self.root:
                break
        self.root.color = BLACK
        return rotation_count, color_changes_count

    def fix_delete(self, x):
        color_changes_count = 0
        rotation_count = 0
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    rotation_count += 1
                    w = x.parent.right
                    color_changes_count += 1
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                    color_changes_count += 1
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        rotation_count += 1
                        w = x.parent.right
                        color_changes_count += 1
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.parent)
                    rotation_count += 1
                    x = self.root
                    color_changes_count += 1
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    rotation_count += 1
                    w = x.parent.left
                    color_changes_count += 1
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                    color_changes_count += 1
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        rotation_count += 1
                        w = x.parent.left
                        color_changes_count += 1
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.parent)
                    rotation_count += 1
                    x = self.root
                    color_changes_count += 1
        x.color = BLACK
        return rotation_count, color_changes_count

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.nil:
            node = node.right
        return node