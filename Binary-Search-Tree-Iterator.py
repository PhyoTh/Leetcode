# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        print("This is root ---> ", root)
        self.counter = -1
        self.in_order_lst = []
        self.in_order_traverse(root)
        print("This is in_order_lst ---> ", self.in_order_lst)

    def in_order_traverse(self, root):
        if root is None:
            return root

        self.in_order_traverse(root.left)
        self.in_order_lst.append(root.val)
        self.in_order_traverse(root.right)

    def next(self) -> int:
        self.counter += 1
        return self.in_order_lst[self.counter]

    def hasNext(self) -> bool:
        return self.counter < len(self.in_order_lst) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()