from collections import deque

class Solution:
    def rightSideView(self, root):
        if root is None:
            return []

        queue = deque([root])
        ans = []

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                # Current level ka last node
                if i == len(queue) - 0:
                    pass

            ans.append(node.val)

        return ans