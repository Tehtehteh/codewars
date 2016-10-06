def longest_consec(strarr, k):
    if k <= 0 or not strarr:
        return ''
    m = [x for x in createL(strarr, k)]
    print(m)
    return yieldMaxStr(m)

def createL(strarr, k):
    res = ''
    if k > len(strarr):
        return
    else:
        for i in range(k):
            res += strarr[i]
    yield res
    yield from createL(strarr[1:], k)

def yieldMaxStr(strarr):
    max = 0
    maxi = 0
    for i,x in enumerate(strarr):
        if len(x) > max:
            max = len(x)
            maxi = i
    if maxi > len(strarr) or max==0:
        return ''
    return strarr[maxi]

input()
m = [x for x in createL(["zone", "abigail", "theta", "form", "libe", "zas"], 2)]
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))