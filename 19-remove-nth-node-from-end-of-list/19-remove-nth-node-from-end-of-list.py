# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # define 3 pointers, 2 at the head and 1 "previous" pointer at None
        start, left, right = head, head, head
        prev = None # this keep tracks of the node before the left pointer

        if not left:
            return None
        
        # move the right pointer n nodes ahead
        for _ in range(n):
            if not right:
                return None
            right = right.next
        
        # move the 3 pointers till the right pointer reaches the end of the list
        while right:
            prev = left
            left = left.next
            right = right.next
        
        # after the above loop, the left pointer will point to the node to be deleted
        # delete the node at the left pointer 
        if not prev:
            start = left.next # edge case to delete the node at head
        else:
            prev.next = left.next
        
        return start