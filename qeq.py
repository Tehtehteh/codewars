ver1 = '2.3-8'
ver2 = '2.21-7'
ver3 = '12.1-0'

def cmpV(ver1, ver2):
    f1 = ver1.split('.')
    f2 = ver2.split('.')
    f11 = f1[1].split('-')
    f22 = f2[1].split('-')
    print(f1,f2,f11,f22)
    if int(f1[0]) > int(f2[0]):
        return True
    elif int(f1[0]) > int(f2[0]):
        return False
    else:
        g = list(zip(f11, f22))
        if g[0][0] > g[0][1]:
            return True
        elif g[0][0] < g[0][1]:
            return False
        else:
            if g[1][0] > g[1][1]:
                return True
            elif g[1][0] < g[1][1]:
                return False

print(cmpV(ver2,ver1))

#g = list(zip(ver1.split('.')[1].split('-'), ver2.split('.')[1].split('-')))

#print(g)

#print(g[0][0] > g[0][1])
