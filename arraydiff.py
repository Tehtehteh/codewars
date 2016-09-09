def array_diff(a, b):
    for x in b:
        try:
            while a.index(x)>=0:
                a.remove(x)
        except:
            pass
    return a
print(array_diff([1,2], [1]))