import unittest
import numpy as np
from tree.tree import Tree, node


class test_bineary_tree(unittest.TestCase):

    def test_binary_tree_1(self):

        a = node(1, None, None)
        t = Tree(a)

        assert (t.print_binary_tree()) == ['1']

    def test_binary_tree_2(self):

        a = node(1, None, None)
        b = node(7, None, None)
        c = node(5, None, None)
        d = node(4, None, None)
        e = node(2, a, d)
        f = node(3, b, c)
        h = node(10, e, f)

        t = Tree(h)

        assert np.mean(t.print_binary_tree() == np.array([['|', '|',  '|', '10',  '|',  '|',  '|'],
                                                         ['|',  '2', '|',  '|',  '|',  '3',  '|'],
                                                         ['1',  '|', '4',  '|',  '7',  '|',
                                                          '5']])) == 1.

    def test_binary_tree_3(self):

        a = node(1, None, None)
        b = node(7, a, None)
        c = node(5, b, None)
        d = node(3, c, None)

        t = Tree(d)

        assert np.mean(t.print_binary_tree() == np.array([['|', '|', '|', '|', '|', '|', '|', '3',
                                                           '|', '|', '|', '|', '|', '|', '|'],
                                                          ['|', '|', '|', '5', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|', '|'],
                                                          ['|', '7', '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|', '|'],
                                                          ['1', '|', '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|']])) == 1.

    def test_binary_tree_4(self):

        a = node(1, None, None)
        b = node(7, a, None)
        c = node(5, b, None)
        d = node(2, None, None)
        e = node(3, c, d)
        f = node(5, e, None)

        t = Tree(f)

        assert np.mean(t.print_binary_tree() == np.array([['|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '5', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|'],
                                                          ['|', '|', '|', '|', '|',
                                                           '|', '|', '3', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|'],
                                                          ['|', '|', '|', '5', '|', '|',
                                                           '|', '|', '|', '|', '|', '2',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|'],
                                                          ['|', '7', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|'],
                                                          ['1', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|', '|', '|', '|', '|', '|',
                                                           '|']])) == 1.0
