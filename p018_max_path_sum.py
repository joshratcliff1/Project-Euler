def read_triangle():
    with open("p18_input.txt", "r") as f:
        # reads the file and converts to a list of lists.
        matrix = [line.split() for line in f]
        # Then converts each element in the list to an integer
        matrix = [[int(j) for j in i] for i in matrix]
        print("matrix after read", matrix)
        return matrix


def initial_check(matrix, length):
    height = (len(matrix))
    if length > height:
        print("length parameter too large")
        return
    max_position = 0
    max_sum = 0
    for t in range(length+1):
        i = length
        j = t
        curr_sum = matrix[i][j]
        print(matrix[i][j])
        while i > 0:
            if j == 0:
                i -= 1
            elif j == i:
                i -= 1
                j -= 1
            elif matrix[i-1][j-1] >= matrix[i-1][j]:
                i -= 1
                j -= 1
            else:
                i -= 1
            print(matrix[i][j])
            curr_sum += matrix[i][j]
        print("position =",t)
        print("curr_sum =",curr_sum)
        if curr_sum > max_sum:
            max_position = t
            max_sum = curr_sum
    return max_position, max_sum


print(initial_check(read_triangle(), 3))


def final_check(matrix, length, curr_sum):
    height = (len(matrix))
    if height > length:
        print("length parameter to large")
        return
    position = 0
    sum = curr_sum
    print("sum at commencemet of final check=", sum)
    for i in range(1, height):
        print(matrix[i])
        if matrix[i][position] >= matrix[i][position + 1]:
            print(matrix[i][position])
            sum += matrix[i][position]
        else:
            position += 1
            print(matrix[i][position])
            sum += matrix[i][position]

    print("sum =", sum)
