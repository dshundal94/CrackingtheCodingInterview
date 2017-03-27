#Problem 1.7 Rotate Matrix: Given an image represented by an N x N matrix, where each pixel in 
#the image is 4 bytes, write a method to rotae image by 90 degrees(I'm going to do it clockwise)
#Can you do this in place?

def rotateMatrix(matrix):
    size = len(matrix)
    for layer in range(size // 2):
        first, last = layer, size - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    print matrix



rotateMatrix([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])