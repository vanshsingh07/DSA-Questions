class Solution:
    def pathSum(self, root, targetSum):
        ans = []

        def dfs(node, target, path):
            if node is None:
                return

            path.append(node.val)
            target -= node.val

            # Leaf node
            if node.left is None and node.right is None:
                if target == 0:
                    ans.append(path[:])

            dfs(node.left, target, path)
            dfs(node.right, target, path)

            path.pop()

        dfs(root, targetSum, [])

        return ans