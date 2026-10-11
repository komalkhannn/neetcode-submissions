# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = [] 
        
        if root is None:
            return result

        q = collections.deque()
        q.append(root)

        while q:
            levelSize = len(q)
            currentLevel = []

            for i in range (levelSize):
                currentNode = q.popleft()
                if currentNode:
                    currentLevel.append(currentNode.val)
                    q.append(currentNode.left)
                    q.append(currentNode.right)

            if currentLevel:
                result.append(currentLevel)
        return result