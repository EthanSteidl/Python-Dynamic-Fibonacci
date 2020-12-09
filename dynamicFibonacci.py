def dynamicFibonacci(n):
    table = [0,1]
    if(n<2):
        return table[n]
    for i in range(2,n+1):
        table.append(table[i-1] + table[i-2])
    return table[n]