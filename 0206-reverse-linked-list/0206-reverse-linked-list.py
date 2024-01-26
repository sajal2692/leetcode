# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # iterative solution
        # prev, curr = None, head
        # while curr:
        #     # create a temp var to track the next of current
        #     temp = curr.next
        #     # point current to previous
        #     curr.next = prev
        #     # move previous pointer to current
        #     prev = curr
        #     # move current pointer to the temp node (which points to the next one)
        #     curr = temp
        # return prev
        
        # recursive solution 1
        
        # base case
        if not head: # to capture empty list case
            return None
        
        # recursive case
        newHead = head # to capture single item in list case
        # the meat of the code
        if head.next:
            # whatever is the next node in the list is the new head
            newHead = self.reverseList(head.next)
            # moving back up the stack
            # reverse the pointers
            head.next.next = head
            # remove the original next pointer for the current head
            head.next = None
            
        return newHead

# easier to understand recursive solution
    def reverseList(self, node: Optional[ListNode],  prev: Optional[ListNode]=None) -> Optional[ListNode]:
        
        # base case
        if not node:
            return prev
        
        # recursive case
        next = node.next
        node.next = prev
        return self.reverseList(node=next, prev=node)