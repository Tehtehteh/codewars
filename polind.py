MIN = 100
MAX=1000
lstr = str
def is_pol(num):
    if lstr(num)==lstr(num)[::-1]:
        return True
    else: return False

def pol():
    mx = 0
    for i in range(MAX-1, MIN, -1):
        for j in range(MAX-1, i-1, -1):
            ml = i*j
            if ml>mx and is_pol(ml):
                mx = ml
    return mx

print(pol())