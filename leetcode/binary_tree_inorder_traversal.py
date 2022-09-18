from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        """ Generate TreeNode string representation
        Format: [[right_node_value, node_value, left_node_value], [right_node_value, node_value, left_node_value], ...]
         """
        list = []
        current = self
        while current.right is not None:
            list.append([current.left.val if current.left else None,current.val,
                        current.right.val if current.right else None])
            current = current.right
        list.append([current.left.val if current.left else None,current.val,
                    current.right.val if current.right else None])
        return str(list)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if root != None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

def gen_tree(list_values: list):
    if len(list_values) == 0:
        return TreeNode()
    root = TreeNode(val=list_values.pop(0), left=None, right=None)
    for i in list_values:
        current = root
        while current.right is not None:
            current = current.right
        new_node = TreeNode(i)
        new_node.left = current
        current.right = new_node
    return root

# gen_tree([None, 1,2,3,None,4])
sol = Solution()
sol.inorderTraversal(gen_tree([]))
    