from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            result.append(queue[0].val)

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
    
        return result


def get_root(adj: list[int], idx: int = 0) -> TreeNode | None:
    node = None

    if idx < len(adj) and adj[idx]:
        val = adj[idx]
        left = get_root(adj, 2 * idx + 1)
        right = get_root(adj, 2 * idx + 2)

        node = TreeNode(val, left, right)

    return node


s = Solution()

tests = [
    [1, 2, 3, None, 5, None, 4],
    [1, 2, 3, 4, None, None, None, 5],
    [1, None, 3],
    [],
]

for adj in tests:
    root = get_root(adj)
    print(s.rightSideView(root))
