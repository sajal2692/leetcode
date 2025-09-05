class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        # initialise the linked list at a dummyy node
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return curr.val if curr else -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        i = 0
        curr = self.head
        while curr and i < index: 
            i += 1
            curr = curr.next
        if curr:
            new_node = Node(val)
            new_node.next = curr.next
            if self.tail == curr:
                self.tail = new_node
            curr.next = new_node


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if self.tail == curr.next:
                self.tail = curr
            curr.next = curr.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)