import time
start_time_t = time.time()

def Collatz_check(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        elif n % 2 == 1:
            n = 3*n + 1
            count += 1
    #print("count=",count)
    return count

def Collatz(tot):
    max = 0
    for i in range(tot-1,tot//2,-2):
        #print("i=",i)
        check = Collatz_check(i)
        if check > max:
            max = check
            ret = i
    print("longest chain =",max)
    print("starting number =",ret)

Collatz(1000000)

#longest chain = 525
#starting number = 837799
#--- 13.272320032119751 actual seconds ---


print("--- %s actual seconds ---" % (time.time() - start_time_t))