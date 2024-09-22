import sys

input = lambda: sys.stdin.readline().rstrip()

tree = {}

N = int(input())
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = (left, right)


def traverse_preorder(parent):
    if parent == ".":
        return ""
    return (parent
            + traverse_preorder(tree[parent][0])
            + traverse_preorder(tree[parent][1]))


def traverse_inorder(parent):
    if parent == ".":
        return ""
    return (traverse_inorder(tree[parent][0])
            + parent
            + traverse_inorder(tree[parent][1]))


def traverse_postorder(parent):
    if parent == ".":
        return ""
    return (traverse_postorder(tree[parent][0])
            + traverse_postorder(tree[parent][1])
            + parent)


print(traverse_preorder("A"))
print(traverse_inorder("A"))
print(traverse_postorder("A"))
