def Fibonacci(n):
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer'
    if n in [0,1]:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(1.5))