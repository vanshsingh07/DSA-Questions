class Solution:
    def maxPathSum(self, root):
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path jo current node se pass ho raha hai
            current = node.val + left + right

            ans = max(ans, current)

            # Parent ko sirf ek side ka path de sakte hain
            return node.val + max(left, right)

        dfs(root)

        return ans