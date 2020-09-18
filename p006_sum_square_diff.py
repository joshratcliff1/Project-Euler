import time
start_time_t = time.time()

def sum_squares(n):
    result = 0
    for i in range(1,n+1):
        result += i**2
    return result

def square_sum(n):
    result = 0
    for i in range(1,n+1):
        result += i
    result = result**2
    return result


a = sum_squares(100)
b = square_sum(100)
c = b - a

print(a)
print(b)
print(c)

print("--- %s actual seconds ---" % (time.time() - start_time_t))