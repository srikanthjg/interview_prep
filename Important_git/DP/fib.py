

#recursive

def fib(n,memo):
    if memo[n]!=-1:
        return memo[n]

    if n<=1:
        memo[n]=n
        return n
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]

def fib_iterative(n):
    if n<=1:
        return n
    fib=[-1 for i in range(n)]
    fib[0]=0
    fib[1]=1
    for i in range(2,n):
        fib[i]=fib[i-1]+fib[i-2]
    print fib
    return fib[n-1]

n=6
memo=[-1 for i in range(n)]
print fib(n,memo)
print memo
print fib_iterative(n)
