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

    def delete(self, val, all=False): #метод удаления одного узла по его значению
        node = self.head
        old = self.head
        while node != None:
            if node.value == val:
                if node == self.head and node == self.tail and node.value == val:
                    self.head = self.tail = None
                if node == self.head:
                    self.head = node.next
                if node == self.tail:
                    self.tail = old
                old.next = node.next
                if all == False:
                    return
            else:
                old = node
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

    def insert(self, afterNode, newNode): #метод вставки узла после заданного узла
        if afterNode == None and self.head == None and self.tail == None:
            if type(newNode) == Node:
                LinkedList.add_in_tail(self, newNode) # проверка на пустой список
            if type(newNode) == int:
                self.tail = self.head = Node(newNode)
            return
        node = self.head
        while True:
            if type(newNode) == Node:
                LinkedList.add_in_tail(self, newNode)
                return
            if type(newNode) == int and type(afterNode) == Node:
                if node.value == afterNode.value:
                    node.next = Node(newNode, node.next)
                    if node.next.next == None:
                        self.tail = node.next
                    break
                else: node = node.next
            if type(newNode) == int and type(afterNode) == int:
                if node.value == afterNode:
                    node.next = Node(newNode, node.next)
                    if node.next.next == None:
                        self.tail = node.next
                    break
                else: node = node.next
