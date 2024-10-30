from src import TreeNode

def max_depth_recursive (root: TreeNode) -> int:
    if not root:
        return 0
    
    return 1 + max(max_depth_recursive(root.left), max_depth_recursive(root.right))

def max_depth_iterative (root: TreeNode) -> int:
    if not root:
        return 0

    max_depth = 0
    stack = []
    visiteds = set()
    cur = root

    while cur or stack:

        while cur and cur not in visiteds:
            stack.append(cur)
            visiteds.add(cur)
            cur = cur.left

        max_depth = max(max_depth, len(stack))
        
        cur = stack[-1]

        if cur.right and cur.right not in visiteds:
            cur = cur.right
        else:
            stack.pop()
            cur = None

        
        
    return max_depth