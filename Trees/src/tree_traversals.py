from typing import List
from src import TreeNode
        
def preOrderTraverseRecursive(root: TreeNode) -> List[int]:
    result = []

    def dfs(node: TreeNode):
        if not node:
            return
        
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result

def inOrderTraverseRecursive(root: TreeNode) -> List[int]:
    result = []

    def dfs(node: TreeNode):
        if not node:
            return
        
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result

def postOrderTraverseRecursive(root: TreeNode) -> List[int]:
    result = []

    def dfs(node: TreeNode):
        if not node:
            return
        
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    
    dfs(root)
    return result

def preOrderTraverseIterative(root: TreeNode) -> List[int]:
    if not root:
        return []

    result = []
    stack = [root]
    stack2 = [root.val]

    while stack:
        cur = stack[-1]
        
        while cur:
            result.append(cur.val)

            if not cur.left:
                break
            stack.append(cur.left)
            stack2.append(cur.left.val)
            cur = cur.left        

        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
                stack2.append(cur.right.val)
                break
    
    return result

def inOrderTraverseIterative(root: TreeNode) -> List[int]:
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        cur = stack[-1]
        
        while cur:

            if not cur.left:
                break
            stack.append(cur.left)
            cur = cur.left        

        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
                break
    
    return result

def postOrderTraverseIterative(root: TreeNode) -> List[int]:
    if not root:
        return []

    result = []
    stack = [root]
    stack2 = []

    while stack:
        cur = stack.pop()
        stack2.append(cur)

        if cur.left:
            stack.append(cur.left)
        
        if cur.right:
            stack.append(cur.right)  
       
    
    while stack2:
        result.append(stack2.pop().val)
        
    return result


def postOrderTraverseIterativeOneStack(root: TreeNode) -> List[int]:
    if not root:
        return []

    result = []
    stack = []
    visiteds = set()
    cur = root

    while cur or stack:

        while cur and cur not in visiteds:
            stack.append(cur)
            visiteds.add(cur)
            cur = cur.left
        
        cur = stack[-1]

        if cur.right and cur.right not in visiteds:
            cur = cur.right

        else:
            result.append(stack.pop().val)
            cur = None

        
        
    return result