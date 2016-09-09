def Descending_Order(num):
    g = []
    retN = ''
    for x in str(num):
        g.append(x)
    if len(g) == 1:
        return int(g[0])
    for x in reversed(g):
        retN += x
    return int(retN)
