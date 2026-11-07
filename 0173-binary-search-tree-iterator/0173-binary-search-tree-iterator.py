# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left   

    def next(self) -> int:
        curr = self.stack.pop()
        res = curr.val
        curr = curr.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return res

    def hasNext(self) -> bool:
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()