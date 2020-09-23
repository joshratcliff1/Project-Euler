from random import choices as rc
import time
start_time_t = time.time()


def read_triangle():
    """
    Reads the input file and converts it into a list of lists.
    Each row is a new element in the outer list.
    Each element of the row is inside the inner list
    :return: triangle list is a formatted list of lists.
    """
    with open("p067_input.txt", "r") as fh:
        # reads the file and converts to a list of lists.
        triangle_list = [line.split() for line in fh]
        # Then converts each element in the list to an integer
        triangle_list = [[int(j) for j in i] for i in triangle_list]
        return triangle_list


def weighted_traverse_forwards(triangle):
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

    return (traversal, next_element)


def weighted_traverse_backwards(triangle, element_distribution):
    """
    Performs a single traversal of the triangle and outputs the result.
    The path of the traversal is determined by a randomly weighted selection.
    ie. if there were two options of 80 and 20. 80 would be selected 80% of the time.

    :param triangle: Reads in the triangle list of list
    :return: Returns the traversal of this attempt
    """
    triangle_height = len(triangle)

    start_choice = range(triangle_height)
    start_weight_choice = element_distribution
    #start_weight_choice[53] += 100
    #start_weight_choice[57] += 50
    #start_weight_choice[44] += 30
    #start_weight_choice[59] += 20
    #start_weight_choice[62] += 10
    #print("weight choice is {}".format(start_weight_choice))

    next_element = rc(start_choice, weights=start_weight_choice)[0]
    #print(triangle[triangle_height-1][next_element])
    traversal = [triangle[triangle_height-1][next_element]]

    # Step down through each row. Decide next element by weighted choice (unless on edges of triangle).
    for row in range(triangle_height-1,0,-1):
        #print("row is {}".format(row))
        #print("next element is {}".format(next_element))
        if next_element == 0:
            next_element = 0
        elif next_element == row:
            next_element -= 1
        else:
            choice = [next_element, next_element-1]
            weight_choice = [triangle[row-1][next_element], triangle[row-1][next_element-1]]
            next_element = rc(choice, weights=weight_choice)[0]

        traversal.append(triangle[row-1][next_element])

    return traversal


def iterate_forwards(n):
    """
    Iterates through the specified number of attempts. Keeps a track of the maximum sum and the traversal
    that produced the maximum sum.

    The current best attempts are printed to console as a side-effect.
    :param n: The number of iterations to attempt.
    :return:
    """
    triangle = read_triangle()
    max_sum = 0
    element_distribution = [1 for x in range(100)]

    for i in range(n):
        if i % 100000 == 0 and i > 0:
            print("F iteration {}".format(i))

        (traversal, element) = weighted_traverse_forwards(triangle)
        element_distribution[element] += 1
        if sum(traversal) > max_sum:
            max_sum = sum(traversal)
            print("F iteration {}. Max sum is {} for traversal {}".format(i, max_sum, traversal))

    print(element_distribution)
    return element_distribution


def iterate_backwards(n, element_distribution):
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
        if i % 100000 == 0 and i > 0:
            print("B iteration {}".format(i))

        traversal = weighted_traverse_backwards(triangle, element_distribution)
        if sum(traversal) > max_sum:
            max_sum = sum(traversal)
            print("B iteration {}. Max sum is {} for traversal {}".format(i, max_sum, traversal))


nf = 10000000
nb = 5000000

element_distribution = iterate_forwards(nf)

iterate_backwards(nb, element_distribution)

print("--- %s actual seconds ---" % (time.time() - start_time_t))