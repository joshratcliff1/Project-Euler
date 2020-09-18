import time
start_time_t = time.time()

def prime_factors(x):
    i = 2
    while i < x+1:
        if x % i == 0:
            print("factor =",i)
            x /= i
            i = 2
        elif i % 2 == 1:
            i += 2
        else:
            i += 1

prime_factors(600851475143)

print("--- %s actual seconds ---" % (time.time() - start_time_t))