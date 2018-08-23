import numpy as np


class Tree():
    def __init__(self, node=None):
        self.root = node
        self.depth = None

    def print_binary_tree(self):

        def get_max_depth(leaf):
            if not leaf:
                return 0
            return 1 + max(get_max_depth(leaf.left), get_max_depth(leaf.right))

        depth = get_max_depth(self.root)
        cols = 2 ** depth - 1
        res = [['|' for i in range(cols)] for i in range(depth)]

        def traverse(node, level, pos):
            if not node:
                return
            left_padding, spacing = 2 ** (depth - level - 1) - 1, 2 ** (depth - level) - 1
            index = left_padding + pos * (spacing + 1)
            res[level][index] = str(node.value)
            traverse(node.left, level + 1, pos << 1)
            traverse(node.right, level + 1, (pos << 1) + 1)

        traverse(self.root, 0, 0)
        # print(np.array(res))
        return np.array(res)


class node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
