from collections import deque


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    if node is None:
        return None
    root = None
    queue = deque([(node, None)])
    visited = {}
    while len(queue) != 0:
        node_tuple = queue.popleft()
        no = node_tuple[0]
        parent = node_tuple[1]
        new_node = Node(no.val)
        visited[no] = new_node
        if root is None:
            root = new_node
        if parent is not None:
            parent.neighbors.append(new_node)
        for n in no.neighbors:
            if n in visited:
                new_node.neighbors.append(visited[n])
            else:
                queue.append((n, new_node))
    return root


cloneGraph(Node(1))
