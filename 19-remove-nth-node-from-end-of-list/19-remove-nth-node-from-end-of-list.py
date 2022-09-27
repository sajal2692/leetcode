# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # define a dummy node that points to the head of the list
        left = dummy # the left pointer starts at the dummy node
        right = head # the right pointer starts at the head
        
        # move the right pointer by n nodes
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # move the left and right pointers till the right pointer reaches the end of the list
        while right:
            left = left.next
            right = right.next
            
        # since left started at the dummy node, skip the node after "left" (this is the one to be deleted)
        left.next = left.next.next
        
        return dummy.next
        
        
        