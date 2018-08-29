def a():
    sum = 0

    n = int(input())
    l = []
    get_values = input()
    l = get_values.split()

    for i in range(n):
            sum=sum +int(l[i])
    return(sum)
        
