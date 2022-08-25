def collatz(n):
    n = int(n)
    lst = []
    while n>1:
        lst.append(n)
        # print(n,type(n))
        if n%2 == 0: 
            n=int(n//2)
        else:
            n=int(n*3+1)
        if n==1: 
            lst.append(n)
    print(len(lst))
    return len(lst)

collatz(73567465519280238573)