def accum(s):
    s1 = ''
    for i,x in enumerate(s):
        s1 = s1 + x.upper()*1+ (x.lower()*i)
        s1+='-'
    return s1[:-1]

print(accum('ZpglnRxqenU'))
