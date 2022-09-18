from binary_tree_inorder_traversal import Solution
from binary_tree_inorder_traversal import TreeNode
from binary_tree_inorder_traversal import gen_tree


def test_binary_tree_inorder_traversal():
    sol = Solution()
    treeSet1 = gen_tree([1,None,2,3])
    # treeSet2 = gen_tree([])
    # treeSet3 = gen_tree([1])
    treeSet4 = gen_tree([1,2,3,4,5,6])
    assert sol.inorderTraversal(treeSet1) == [1,3,2]
    # assert sol.inorderTraversal(treeSet2) == []
    # assert sol.inorderTraversal(treeSet3) == [1]
    assert sol.inorderTraversal(treeSet4) == [4,2,5,1,6,3]