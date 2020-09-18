# check for zero remainder when dividing by x and y.
# Z is the maximum number to check until.
# continue adding to the sum
def multiples(x, y, z):
    sum = 0
    for i in range(z):
        if i % x == 0:
            sum = sum + i
        elif i % y == 0:
            sum = sum + i
    print(sum)


multiples(3, 5, 1000)
