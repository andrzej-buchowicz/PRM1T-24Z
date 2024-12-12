import timeit

import matplotlib.pylab as plt


llist_setup = """
import random

from data_struct.linked_list import LinkedList, Element

llist = LinkedList()
for i in range(n):
    llist.append(Element(random.randint(0, 10 * n)))
"""

llist_code = """
index = llist.find(Element(random.randint(0, 10 * n)))
"""

btree_setup = """
import random

from data_struct.binary_search_tree import BinarySearchTree, Node

btree = BinarySearchTree()
for i in range(n):
    btree.insert(Node(random.randint(0, 10 * n)))
"""

btree_code = """
result = btree.search(random.randint(0, 10 * n))
"""


N = [100, 200, 400, 800, 1600]
llist_time = []
btree_time = []
for n in N:
    llist_time.append(timeit.timeit(llist_code, setup=llist_setup, number=10000, globals=globals()))
    btree_time.append(timeit.timeit(btree_code, setup=btree_setup, number=10000, globals=globals()))

print("LinkedList: ", llist_time)
print("BinarySearchTree: ", btree_time)

_, ax = plt.subplots()
ax.plot(N, llist_time, marker='.', label="LinkedList")
ax.plot(N, btree_time, marker='.', label="BinaryTree")
ax.set_xlabel('N')
ax.set_ylabel('t [s]')
ax.legend()
ax.grid()
plt.show()
