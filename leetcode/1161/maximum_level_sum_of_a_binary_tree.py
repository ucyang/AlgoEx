from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        queue = deque([root])

        max_sum = root.val
        max_level = 1
        level = 1

        while queue:
            sum_of_level = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                sum_of_level += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if sum_of_level > max_sum:
                max_sum = sum_of_level
                max_level = level

            level += 1

        return max_level


def get_root(adj: list[int], idx: int = 0) -> TreeNode | None:
    node = None

    if idx < len(adj) and adj[idx] is not None:
        val = adj[idx]
        left = get_root(adj, 2 * idx + 1)
        right = get_root(adj, 2 * idx + 2)

        node = TreeNode(val, left, right)

    return node


s = Solution()

tests = [
    [1, 7, 0, 7, -8, None, None],
    [989, None, 10250, 98693, -89388, None, None, None, -32127],
]

for adj in tests:
    root = get_root(adj)
    print(s.maxLevelSum(root))
