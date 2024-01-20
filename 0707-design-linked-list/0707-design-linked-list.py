class ListNode:
    
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            return curr.val
        return -1
        
    def addAtHead(self, val: int) -> None:
        new, prev, next = ListNode(val), self.left, self.left.next
        new.next = next
        new.prev = prev
        prev.next = new
        next.prev = new

    def addAtTail(self, val: int) -> None:
        new, prev, next = ListNode(val), self.right.prev, self.right
        new.next = next
        new.prev = prev
        prev.next = new
        next.prev = new
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            new, prev, next = ListNode(val), curr.prev, curr
            new.next = next
            new.prev = prev
            prev.next = new
            next.prev = new
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            prev, next = curr.prev, curr.next
            prev.next = next
            next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)