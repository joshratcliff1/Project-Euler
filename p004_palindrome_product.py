import time
start_time_t = time.time()

def palindrome_product(x):
    # using map to create a list and then a backwards list
    # to convert number to list of integers
    # using // to not have to itterate through all possibilities
    # compare if the two lists are the same and then save the result
    result = 0
    for num1 in range(x//2,x+1):
        for num2 in range(x//2,x+1):
            product = num1 * num2
            L_f = list(map(int, str(product)))
            L_b = L_f[::-1]
            if L_f == L_b:
                if product > result:
                    result = product
    print("largest palindrome is",result)

palindrome_product(999)

print("--- %s actual seconds ---" % (time.time() - start_time_t))