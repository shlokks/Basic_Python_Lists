def aVeryBigSum():
    l = []
    sum = 0
    n = int(input())
    get_values = input()
    l = get_values.split()
    
    for i in range(n):
        sum = sum + l[i]
        
    return(sum)
    
    

        
