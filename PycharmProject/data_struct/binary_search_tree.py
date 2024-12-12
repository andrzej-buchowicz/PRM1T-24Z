class Node:
    def __init__(self, value):
        assert isinstance(value, (int, float))
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        assert isinstance(node, Node)
        if node.value == self.value:  # do not duplicate the same values
            return
        elif node.value < self.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
                return
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
                return

    def search(self, value):
        assert isinstance(value, (int, float))
        if value == self.value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def __str__(self):
        text = ""
        if self.left:
            text += str(self.left)
        text += "<" + str(self.value) + ">"
        if self.right:
            text += str(self.right)
        return text


class BinarySearchTree:
    def __init__(self, root=None):
        assert isinstance(root, Node) or root is None
        self.root = root

    def insert(self, node):
        assert isinstance(node, Node)
        if self.root:
            self.root.insert(node)
        else:
            self.root = node

    def search(self, value):
        return self.root.search(value)

    def __str__(self):
        if self.root:
            return self.root.__str__()
        else:
            return "..."


def main():
    node = Node(123)
    print(node)

    bst = BinarySearchTree()
    print(bst)

    bst.insert(Node(1))
    print(bst)

    bst.insert(Node(4))
    print(bst)

    bst.insert(Node(7))
    print(bst)

    bst.insert(Node(3))
    print(bst)

    print(bst.search(1))
    print(bst.search(4))
    print(bst.search(5))
    print(bst.search(6))


if __name__ == "__main__":
    main()
