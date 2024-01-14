# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # create a temp var to track the next of current
            temp = curr.next
            # point current to previous
            curr.next = prev
            # move previous pointer to current
            prev = curr
            # move current pointer to the temp node (which points to the next one)
            curr = temp
        return prev
            
            