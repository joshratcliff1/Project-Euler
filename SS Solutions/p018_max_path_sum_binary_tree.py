# https://www.geeksforgeeks.org/binary-tree-set-1-introduction/

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key



def read_triangle():
    with open("../p018_input.txt", "r") as fh:
        # reads the file and converts to a list of lists.
        matrix = [line.split() for line in fh]
        # Then converts each element in the list to an integer
        matrix = [[int(j) for j in i] for i in matrix]
        #print("matrix after read {}".format(matrix))
        return matrix

triangle = read_triangle()

print(triangle)

'''
for line in range(len(triangle)):
    for num in range(len(triangle[line])):
        if line == 0:
            root = Node(num)
        else:

'''

root = Node(1)


