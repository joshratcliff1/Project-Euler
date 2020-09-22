from random import choices as rc


def read_triangle():
    """
    Reads the input file and converts it into a list of lists.
    Each row is a new element in the outer list.
    Each element of the row is inside the inner list
    :return: triangle list is a formatted list of lists.
    """
    with open("p018_input.txt", "r") as fh:
        # reads the file and converts to a list of lists.
        triangle_list = [line.split() for line in fh]
        # Then converts each element in the list to an integer
        triangle_list = [[int(j) for j in i] for i in triangle_list]
        return triangle_list


def weighted_traverse(triangle):
    """
    Performs a single traversal of the triangle and outputs the result.
    The path of the traversal is determined by a randomly weighted selection.
    ie. if there were two options of 80 and 20. 80 would be selected 80% of the time.

    :param triangle: Reads in the triangle list of list
    :return: Returns the traversal of this attempt
    """
    triangle_height = len(triangle)

    next_element = 0
    traversal = [triangle[0][next_element]]

    # Step through each row. Decide next element by weighted choice.
    for row in range(triangle_height-1):

        choices = [next_element, next_element+1]
        weight_choice = [triangle[row+1][next_element], triangle[row+1][next_element+1]]

        next_element = rc(choices, weights=weight_choice)[0]
        traversal.append(triangle[row + 1][next_element])

    return traversal


def iterate(n):
    """
    Iterates through the specified number of attempts. Keeps a track of the maximum sum and the traversal
    that produced the maximum sum.

    The current best attempts are printed to console as a side-effect.
    :param n: The number of iterations to attempt.
    :return:
    """
    triangle = read_triangle()
    max_sum = 0

    for i in range(n):
        if i % 100 == 0 and i > 0:
            print("Iteration {}".format(i))

        traversal = weighted_traverse(triangle)
        if sum(traversal) > max_sum:
            max_sum = sum(traversal)
            print("iteration {}. Max sum is {} for traversal {}".format(i, max_sum, traversal))


iterate(1000)
