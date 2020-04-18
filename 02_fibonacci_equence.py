fibonacciCache={}
def fibonacci(n):
    if n in fibonacciCache:
        return fibonacciCache[n]


    if n==1:
        value=1
    elif n==2:
        value=1
    elif n>2:
        value=fibonacci(n-1)+fibonacci(n-2)

    fibonacciCache[n]=value
    return value


print(6, ":", fibonacci(6))
     
