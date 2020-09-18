def even_fib(x):
    fib_o = 1
    fib_n = 2
    sum = 0
    while fib_n < x:
        print(fib_n)
        if fib_n % 2 == 0:
            sum += fib_n
        fib_t = fib_n
        fib_n += fib_o
        fib_o = fib_t
    print("Sum eqauls",sum)

even_fib(4000000)