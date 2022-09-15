# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # need to keep track of previous, current and next node
        prev = None
        current = head
        
        # iterate through the list
        while current:
            # save the next node to a variable
            # this is important so that after changing the link of the current node to previous,
            # we still keep track of the next node in the list
            nxt = current.next
            # point the current node to the previous element (on first iteration this will be None)
            current.next = prev
            # move previous node pointer forward
            prev = current
            # move the current node pointer forward (pointing it to the previously saved next node variable)
            current = nxt
        # finally, point the head of the list to the previous node
        # note: this will be the last node in the list after the while loop ends
        head = prev
        return head