def getRows(m):
    for x in m:
       if ''.join(y for y in x) == 'XXX':
           yield 'x'
       elif ''.join(y for y in x) == 'OOO':
           yield 'o'
       else:
           yield 'd'

def getColumns(m):
    for x in zip(*m):
       if ''.join(y for y in x) == 'XXX':
               yield 'x'
       elif ''.join(y for y in x) == 'OOO':
           yield 'o'
       else:
           yield 'd'

def getDig(m):
    if ''.join(m[i][i] for i in range(3)) == 'XXX' or ''.join(m[i][i-3+i] for i in range(3)) == 'XXX':
        yield 'x'
    elif ''.join(m[i][i] for i in range(3)) == 'OOO'or ''.join(m[i][i-3+i] for i in range(3)) == 'OOO':
        yield 'o'
    else:
        yield 'd'

m = [
    "X.O",
    "XX.",
    "XOO"]

def main(m):
    g = []
    for x in m:
        (*a,) = x
        g.extend([a])
    ans = []
    ans.extend(x for x in getRows(g))
    ans.extend(x for x in getColumns(g))
    ans.extend(x for x in getDig(g))
    return next(filter(lambda x: x!='d', ans)) if list(filter(lambda x: x!='d', ans)) else 'd'
    
print(main(m))