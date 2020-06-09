class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        find_elem = list()

        while node is not None:
            if node.value == val:
                find_elem.append(node)
            node = node.next
        return find_elem

    def delete(self, val, all=False):
        node = self.head
        prev = self.head

        while node is not None:
            if node.value == val:
                if node == self.head and node == self.tail:
                    self.head = self.tail = None  # Если элемент единственный
                elif node == self.head:
                    self.head = node.next
                elif node == self.tail:
                    self.tail = prev
                    prev.next = None
                else:
                    prev.next = node.next
                if not all:
                    return
            prev = node
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        num = 0
        node = self.head
        while node is not None:
            num += 1
            node = node.next
        return num

    def insert(self, afterNode, newNode):
        if type(afterNode) is not Node:
            afterNode = Node(afterNode)
        if type(newNode) is not Node:
            newNode = Node(newNode)

        if afterNode is None or self.find(afterNode.value) is None:
            if self.head is None and self.tail is None:
                self.add_in_tail(newNode)
                return
            newNode.next = self.head
            self.head = newNode
            return
        elif newNode is None:
            return
        else:
            afterNode = self.find(afterNode.value)
            newNode.next = afterNode.next
            afterNode.next = newNode
