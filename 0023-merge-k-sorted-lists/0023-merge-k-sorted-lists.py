# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge cases
        if len(lists) == 0 or not lists:
            return None
        
        # iterative
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list_1 = lists[i]
                list_2 = lists[i+1] if i+1 < len(lists) else None
                mergedList = self.mergeList(list_1, list_2)
                mergedLists.append(mergedList)
            lists = mergedLists
        
        return lists[0]
        
    # todo merge two lists
    def mergeList(self, list_1, list_2):
        dummy = ListNode(-1)
        curr = dummy
        
        while list_1 and list_2:
            if list_1.val <= list_2.val:
                curr.next = list_1
                list_1 = list_1.next
            else:
                curr.next = list_2
                list_2 = list_2.next
            curr = curr.next
        
        # one of the lists may be remaining
        
        if list_1:
            curr.next = list_1
        
        if list_2:
            curr.next = list_2
        
        return dummy.next
            
        