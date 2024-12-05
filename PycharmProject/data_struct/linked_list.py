class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.index = 0

    def __len__(self):
        curr_elem = self.head
        num_elem = 0
        while curr_elem is not None:
            num_elem += 1
            curr_elem = curr_elem.next
        return num_elem

    def append(self, elem):
        assert isinstance(elem, Element)
        assert elem.next is None

        if self.head is None:
            self.head = elem
            return

        curr_elem = self.head
        while True:
            if curr_elem.next is None:
                break
            curr_elem = curr_elem.next
        curr_elem.next = elem

    def __getitem__(self, index):
        if index < 0 or index >= self.__len__():
            raise IndexError("Index out of bounds")
        curr_elem = self.head
        for i in range(index):
            curr_elem = curr_elem.next
        return curr_elem.value

    def __iter__(self):
        return self

    def __next__(self):
        try:
            elem_value = self.__getitem__(self.index)
        except IndexError:
            raise StopIteration()
        self.index += 1
        return elem_value

    def find(self, elem):
        return -1


def main():
    llist = LinkedList()
    llist.append(Element('a'))
    llist.append(Element('b'))
    llist.append(Element('c'))

    print("Operator indeksowania")
    for index in range(len(llist)):
        print(index, llist[index])

    print("\nIterator")
    for index, elem in enumerate(llist):
        print(index, elem)


if __name__ == "__main__":
    main()




