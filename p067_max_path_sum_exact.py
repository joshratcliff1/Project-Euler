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