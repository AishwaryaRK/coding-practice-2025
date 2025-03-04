# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []


def lowestCommonAncestorTree(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def find_lca(r, p, q):
        if r == None:
            return None, False
        if r.val == p or r.val == q:
            return r, True
        # if find_lca(r.left, p, q) and find_lca(r.right, p, q):
        #     return r
        if r.children:
            nodes = []
            is_nodes = []
            for child in r.children:
                node, is_node = find_lca(child, p, q)
                nodes.append(node)
                is_nodes.append(is_node)
            if sum(is_nodes) == 2:
                return r, True
            for i, is_n in enumerate(is_nodes):
                if is_n:
                    return nodes[i], True
        return None, False

    lca, _ = find_lca(root, p, q)
    return lca.val


root = TreeNode(3)
t1 = TreeNode(5)
t2 = TreeNode(1)
t3 = TreeNode(6)
t4 = TreeNode(2)
t5 = TreeNode(0)
t6 = TreeNode(8)
t7 = TreeNode(7)
t8 = TreeNode(4)
t9 = TreeNode(10)
root.children = [t1, t2]
t1.children = [t3, t4]
t4.children = [t7, t8, t9]
t2.children = [t5, t6]

print(lowestCommonAncestorTree(root, p=5, q=1))
print(lowestCommonAncestorTree(root, p=6, q=4))
print(lowestCommonAncestorTree(root, p=5, q=4))
print(lowestCommonAncestorTree(root, p=7, q=10))
