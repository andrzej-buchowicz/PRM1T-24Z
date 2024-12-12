import unittest

from binary_search_tree import BinarySearchTree, Node


class BinarySearchTreeTestCase(unittest.TestCase):
    def test_find(self):
        btree = BinarySearchTree()
        btree.insert(Node(1))
        btree.insert(Node(4))
        btree.insert(Node(7))
        btree.insert(Node(3))

        self.assertTrue(btree.search(1))
        self.assertFalse(btree.search(2))
        self.assertTrue(btree.search(3))
        self.assertFalse(btree.search(5))
        self.assertTrue(btree.search(7))


if __name__ == '__main__':
    unittest.main()
