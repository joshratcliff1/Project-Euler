import time
start_time_t = time.time()


def read_triangle():
    """
    Reads the input file and converts it into a list of lists.
    Each row is a new element in the outer list.
    Each element of the row is inside the inner list
    :return:
    triangle list: a formatted list of lists of the input triangle.
    blank: A list of lists of same size as the input triangle with each value as zero.
    """
    with open("p067_input.txt", "r") as fh:
        # reads the file and converts to a list of lists.
        triangle_list = [line.split() for line in fh]
        # Then converts each element in the list to an integer
        triangle_list = [[int(j) for j in i] for i in triangle_list]
        blank = [[0 for j in i] for i in triangle_list]
        return triangle_list, blank


def compute_sums(in_triangle, triangle_sums):
    """
    Computes the sum of the best path at each node of the triangle.
    The nodes on the outside edges of the triangle simply sum the value above.
    The inside nodes select the maximum of the two values above.

    :param in_triangle: The original input triangle.
    :param triangle_sums: This triangle is input as a blank triangle.
                          It will be populated with the largest path sum within the function.
    :return: triangle_sums: The populated triangle with the largest path sum.
    """
    for row in range(len(in_triangle)):
        for element in range(len(in_triangle[row])):
            if row == 0:
                triangle_sums[row][element] = in_triangle[row][element]
            elif element == 0:
                triangle_sums[row][element] = in_triangle[row][element] + triangle_sums[row - 1][element]
            elif element == row:
                triangle_sums[row][element] = in_triangle[row][element] + triangle_sums[row - 1][element - 1]
            else:
                triangle_sums[row][element] = in_triangle[row][element] + max(triangle_sums[row - 1][element - 1],
                                                                              triangle_sums[row - 1][element])
    return triangle_sums


# Convert the input text into our list of lists triangle. Also provide a blank triangle of same size
(triangle, blank_triangle) = read_triangle()

# Compute the triangle with the sum of the best route at each position
result_triangle = compute_sums(triangle, blank_triangle)

print(triangle)
print(result_triangle)

# The value of the maximum path value is printed.
print("Sum of largest path is {}".format(max(result_triangle[-1])))

print("--- %s actual seconds ---" % (time.time() - start_time_t))