# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].
# Example 1:
# Input: image = [[1,1,0],
#                 [1,0,1],
#                 [0,0,0]]
# Output: [[1,0,0],
#          [0,1,0],
#          [1,1,1]]
# Explanation: First reverse each row: [[0,1,1],
#                                       [1,0,1],
#                                       [0,0,0]].
# Then, invert the image (all 1s become 0's, and all 0's become 1's: [[1,0,0],
#                                                                     [0,1,0],
#                                                                     [1,1,1]]
# Example 2:
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Constraints:
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.

def matrix_flip(m):
    out = []
    for row in m:
        # print(row)
        new_row = []
        row = row[::-1]
        for pixel in row:
            if pixel == 0:
                new_row.append(1)
            else:
                new_row.append(0)
        out.append(new_row)
    return out


image = [[1,1,0],
         [1,0,1],
         [0,0,0]]

print(matrix_flip(image))
print([[1,0,0],
[0,1,0],
[1,1,1]]
)

image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
output = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
print(matrix_flip(image))
print(output)