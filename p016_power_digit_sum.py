
def power_sum(n,p):
    x = n ** p
    L_f = list(map(int, str(x)))
    print(L_f)
    sum = 0
    for i in L_f:
        sum += i
    print("power sum =",sum)


power_sum(2,1000)