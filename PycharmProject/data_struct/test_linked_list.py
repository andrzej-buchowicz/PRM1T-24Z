import unittest

from linked_list import LinkedList, Element


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.llist = LinkedList()

    def tearDown(self):
        self.llist = None

    def test_append(self):
        self.llist.append((Element(1)))
        self.assertEqual(1, len(self.llist))

        self.llist.append((Element(2)))
        self.assertEqual(2, len(self.llist))

        self.llist.append((Element(3)))
        self.assertEqual(3, len(self.llist))

    def test_index_operator(self):
        self.llist.append(Element('a'))
        self.llist.append(Element('b'))
        self.llist.append(Element('c'))

        self.assertEqual('a', self.llist[0])
        self.assertEqual('b', self.llist[1])
        self.assertEqual('c', self.llist[2])
        self.assertRaises(IndexError, self.llist.__getitem__, -1)
        self.assertRaises(IndexError, self.llist.__getitem__,  3)

    def test_iterator(self):
        self.llist.append(Element('a'))
        self.llist.append(Element('b'))
        self.llist.append(Element('c'))

        llist_iter = iter(self.llist)
        self.assertEqual('a', next(llist_iter))
        self.assertEqual('b', next(llist_iter))
        self.assertEqual('c', next(llist_iter))

    def test_find_elem(self):
        self.llist.append(Element('a'))
        self.llist.append(Element('b'))
        self.llist.append(Element('c'))

        self.assertEqual(0, self.llist.find(Element('a')))
        self.assertEqual(1, self.llist.find(Element('b')))
        self.assertEqual(2, self.llist.find(Element('c')))
        self.assertEqual(-1, self.llist.find(Element('d')))


if __name__ == '__main__':
    unittest.main()
