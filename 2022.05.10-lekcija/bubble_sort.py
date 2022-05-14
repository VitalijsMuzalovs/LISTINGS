def burbulis(array):
    n=len(array)

    for i in range(n):
        already_sorted=True

        for j in range(n-1): #!!!!!
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                already_sorted=False
        if already_sorted:
            break
    return array

print(burbulis([32,86,22,15,94,101,1,55]))