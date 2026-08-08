class Solution:
    def findDiagonalOrder(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        ans = []

        for d in range(rows + cols - 1):
            temp = []

            row = 0 if d < cols else d - cols + 1
            col = d if d < cols else cols - 1

            while row < rows and col >= 0:
                temp.append(mat[row][col])
                row += 1
                col -= 1

            if d % 2 == 0:
                temp.reverse()

            ans.extend(temp)

        return ans