from math import sqrt

def find_square(num,y=1):
    if num // y == y or y == num :
        return y
    else:
        find_square(num,y+1)



print(find_square(16))