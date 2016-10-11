def tower_builder(n_floors):
    res = []
    for i in range(n_floors, 0, -1):
        floor = ' ' * (i//2) + '*' * (n_floors-i+1) + ' ' * (i//2)
        print(floor)
        res.append(floor)
    return res

print(tower_builder(3))