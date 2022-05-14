def Fib(n):
    if n==1 or n==2:
        return 1
    n1=1
    n2=2

    for c in range(3,n+1):
        n1=n1+n2
        n2=n1-n2
    return n1

while 1:
    print('Ievādi vīrknes elementa numuru (0-vēlos beigt darbu)')
    n=int(input())
    if n==0:
        break
    print('Fib(',n,')=',Fib(n))
