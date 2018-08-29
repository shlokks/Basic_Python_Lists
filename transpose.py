def transpose(m):

    a = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return a