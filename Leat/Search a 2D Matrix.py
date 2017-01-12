"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

 Solution: Binary-search.

    bool searchMatrix_2(vector<vector<int> > &matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        int N = matrix.size(), M = matrix[0].size();
        int i = 0, j = M * N - 1;
        while (i <= j)
        {
            int mid = (i + j) / 2;
            int row = mid / M, col = mid % M;
            if (matrix[row][col] == target) return true;
            else if (matrix[row][col] < target) i = mid + 1;
            else j = mid - 1;
        }
        return false;
    }
"""
def searchmat(matrix, target):
    if matrix is [] or matrix is [[]]: return False
    N = len(matrix)
    M = len(matrix[0])
    i=0
    j=M*N-1
    while i<=j:
        mid = (i+j)/2
        row = mid/M
        col= mid % M
        if matrix[row][col] == target: return True
        elif matrix[row][col] < target: i = mid + 1
        else: j = mid - 1
    return  False