class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, rows * columns - 1

        while left <= right:
            middle = (left + right)//2
            row = middle // columns
            col = middle % columns

            if matrix[row][col] < target:
                left = middle + 1
            elif matrix[row][col] > target:
                right = middle - 1
            else:
                return True
        return False



        