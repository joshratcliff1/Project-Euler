import time
import math
start_time_t = time.time()

def smallest_multiple(x):
    #x*(x-1) for the start and the steps reduces the amount of numbers to check
    for check in range(x*(x-1), math.factorial(x), x*(x-1)):
        for j in range(1,x+1):
            # counting from 1, if any numbers aren't a multiple, break and check the next number
            if check % j != 0:
                break
            # if all values pass successfully upto x, then that is the smallest multiple
            elif j == x:
                print("result is",check)
                return

smallest_multiple(20)
# best result 0.6 seconds
print("--- %s actual seconds ---" % (time.time() - start_time_t))




#def smallest_multiple(x):
#    check = x
 #   while check > 1:
  #      for i in range(1,x+1):
   #         if check % i != 0:
    #            break
     #       elif i == x:
      #          print("result is",check)
       #         return
        #    else:
         #       check += 1