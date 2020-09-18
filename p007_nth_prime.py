import time
start_time_t = time.time()

def isprime(n):
    # returns true for primes, false if not.
    if n % 2 == 0:
        return False
    for i in range(3,n-1,2):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    array = [0,2,3]
    test = 5
    while test > 3:
        if isprime(test) == True:
            array.append(test)
        if len(array) == n+1:
            print(array[n])
            return
        test += 2


nth_prime(10001)

#2000th prims is 17389
#9.1 seconds first try
#5.6 seconds after adding test by 2
#1.5 seconds after switching prime function
#0.789 seconds fixed up prime function

#10,001 prime found in 21.96 seconds
print("--- %s actual seconds ---" % (time.time() - start_time_t))